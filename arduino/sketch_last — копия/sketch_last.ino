////////////////////////////////ТЕСТОВЫЙ СТЕНД////////////////////////
///////////////////////////////Библиотеки////////////////////////////
#include <Arduino.h>
#include "GyverIO.h"
#include "GyverDS18.h"
#include "GyverINA.h"
#include "GyverHX711.h"
#include <Servo.h>
#include "EEPROM.h"
//глобальный переменные данных с датчиков:
volatile unsigned long T_flash_E;
volatile unsigned long T_flash_O;
float Temp; 
float ShuntVoltage;
float Voltage;
float Traction;
float Weight_1; 
float Weight_2;
int gas_min = 800; //стандартные значеничя для калибровки регулятора скорости
int gas_max = 2400;
int gas;
///////////////////////////////////////////////////
/*
для принятия данных: ключ (i-gas_min, a-gas_max, o-gas, k-калибровка, t-сброс таймера) значение (int) (при калибровки и сбросе таймера высылать значение 0, после чего оно просто игнорируется)
для отправки данных: значение (int flash_E), разделитель, значение (int flash_O), разделитель, значение (Voltage), разделитель, значение (ShuntVoltage), разделитель, значение(Temp), разделитель, значение (Traction),
разделитель, значение (Weight_1), разделитель, значение (Weight_2), разделитель, значение (mainTime), терминатор
1249,130,094,049,0492, 459;
*/
///////////////////////////////////////////////////
unsigned long mainTime; //переменные таймера 
unsigned long Time;
unsigned long lastflash_E;
unsigned long lastflash_O;
int speed = 9600; //скорость торпа в ботах
INA226 ina(0.001f, 75.0f, 0x40); //подключение ina226
GyverDS18Single ds(16);// пин ds18
GyverHX711 sensor_Traction (6, 7, HX_GAIN128_A); //подключение тензодатчика на тягу
GyverHX711 sensor_Weight_1 (8, 9, HX_GAIN128_A); //подключение тензодатчиков на массу
GyverHX711 sensor_Weight_2 (14, 15, HX_GAIN128_A);
Servo control; //подключение управления мотором
unsigned long lastTime;

void setup() {
  Serial.begin(speed); //открыть монитор порта 

  ds.requestTemp(); //запрос на изменение ds

  if (ina.begin()) {
    ina.setSampleTime(INA226_VBUS, INA226_CONV_4156US ); //Установка времени выборки на 4156 мкс
    ina.setSampleTime(INA226_VSHUNT, INA226_CONV_588US); //Установа времени выборки на 588 мкс
    ina.setAveraging(INA226_AVG_X1); // Усреднение и на ток, и на напряжение в 1 раз
  }
  else {
    while (1);// бесконечный цикл
  }

  pinMode(4, OUTPUT);
  control.attach(5); //пин управлениея мотором 

  EEPROM.get(0, gas_min); //читать из eeprom значение переменной для калибровки
  EEPROM.get(3, gas_max);

  control.writeMicroseconds(gas_max); //калибровка регулятора оборотов
  delay(2000);
  control.writeMicroseconds(gas_min);
  delay(6000);
}

void loop() {

  MotorStarted();

  inputData();

  GetSensWeight();

  GetVoltage();

  GetTraction();

  outData();

  // таймер для последующей передачи в com port
  mainTime = millis() - Time; //счет таймера (перевести в пайчарме)
}

// вывод значений в ком порт
void outData(){
  Serial.print(T_flash_E); Serial.print(","); //отправка данных на пк
  Serial.print(T_flash_O); Serial.print(",");
  Serial.print(Voltage, 3); Serial.print(",");
  Serial.print(ShuntVoltage, 3); Serial.print(",");
  Serial.print(Temp, 2); Serial.print(",");
  Serial.print(Traction, 1); Serial.print(",");
  Serial.print(Weight_1, 1); Serial.print(",");
  Serial.print(Weight_2, 1); Serial.print(",");
  Serial.print(mainTime); Serial.println(";");
}

// получение данных с ком порта
void inputData(){
  if (Serial.available() > 1) { //парсинг данных с пк
    char key = Serial.read();
    int buf = Serial.parseInt();
    switch (key) {
      case 'm': gas_min = buf;
      EEPROM.put(0, gas_min); //
      break;
      case 'x': gas_max = buf;
      EEPROM.put(3, gas_max); //
      break;
      case 'g': gas = buf;
      break; 
      case 'k': 
      EEPROM.get(0, gas_min); //читать из eeprom значение переменной для калибровки
      EEPROM.get(3, gas_max);
      control.writeMicroseconds(gas_max); // калибровка регулятора скорости
      delay(2000);
      control.writeMicroseconds(gas_min);
      delay(6000);
      break;
      case 't': //обнуление таймера 
      Time = millis(); 
      break;
    }
  }

}

// запись показаний датчиков веса
void GetSensWeight(){
  if (sensor_Weight_1.available()) {
    Weight_1 = sensor_Weight_1.read();
  }
  if (sensor_Weight_2.available()) {
    Weight_2 = sensor_Weight_2.read();
  }
}

// запись показаний вольтажа
void GetVoltage(){
  Voltage = ina.getVoltage(); //записать значение напряжения 
  //ShuntVoltage = ina.getShuntVoltage(); //записать значение напряжения на шунте
}

// запись показаний датчика тяги
void GetTraction(){
    if (sensor_Traction.available()) { //если готово
    Traction = sensor_Traction.read() ; //записать значение тяги
  }

}

// подключение и работа мотора
void MotorStarted(){
  if (gas == 0) { //предупреждающий писк перед запуском мотора
    if (gas > 0) { 
    digitalWrite(4, HIGH);
      if (millis() - lastTime > 2000) { //время писка
      lastTime = millis();
      digitalWrite(4, LOW);
      control.writeMicroseconds(gas); // //передать скорость мотора в регулятор 
      }
    }
  } 
  else {
    control.writeMicroseconds(gas); //передать скорость мотора в регулятор 
  }

}

