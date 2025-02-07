////////////////////////////////ТЕСТОВЫЙ СТЕНД////////////////////////
///////////////////////////////Библиотеки////////////////////////////
#include <Arduino.h>
#include "GyverIO.h"
#include "GyverDS18.h"
#include "GyverINA.h"
#include "GyverHX711.h"
#include <Servo.h>
#include "EEPROM.h"

//глобальные переменные данных с датчиков:
volatile unsigned long T_flash_E;
volatile unsigned long T_flash_O;
float Temp; 
float ShuntVoltage;
float Voltage;
float Traction;
float Weight_1; 
float Weight_2;
int gas_min = 800; //стандартные значения для калибровки регулятора скорости
int gas_max = 2400;
int gas;
unsigned long mainTime; //переменные таймера 
unsigned long Time;
unsigned long time;
unsigned long lastflash_E;
unsigned long lastflash_O;
int step = 0; // суммируем
int speed = 9600; //скорость порта в бодах
INA226 ina(0.001f, 75.0f, 0x40); //подключение ina226
GyverDS18Single ds(16); // пин ds18
GyverHX711 sensor_Traction(6, 7, HX_GAIN128_A); //подключение тензодатчика на тягу
GyverHX711 sensor_Weight_1(8, 9, HX_GAIN128_A); //подключение тензодатчиков на массу
GyverHX711 sensor_Weight_2(14, 15, HX_GAIN128_A);
Servo control; //подключение управления мотором
unsigned long lastTime;

void setup() {
  attachInterrupt(0, E_counter_RPM, RISING); // прерывания электронного тахометра, пин D2
  attachInterrupt(1, O_counter_RPM, RISING); // прерывания оптического тахометра, пин D3
  Serial.begin(speed); //открыть монитор порта 
  ds.requestTemp(); //запрос на изменение ds
  
  if (ina.begin()) {
    ina.setSampleTime(INA226_VBUS, INA226_CONV_4156US); //Установка времени выборки на 4156 мкс
    ina.setSampleTime(INA226_VSHUNT, INA226_CONV_588US); //Установа времени выборки на 588 мкс
    ina.setAveraging(INA226_AVG_X1); // Усреднение и на ток, и на напряжение в 1 раз
  } else {
    while (1); // бесконечный цикл
  }
  
  pinMode(4, OUTPUT);
  control.attach(5); //пин управления мотором

  EEPROM.get(0, gas_min); //читать из eeprom значение переменной для калибровки
  EEPROM.get(3, gas_max);
  control.writeMicroseconds(gas_max); //калибровка регулятора оборотов
  delay(2000);
  control.writeMicroseconds(gas_min);
  delay(6000);
}

void loop() {
  if (ds.ready()) { //изменения готовы
    if (ds.readTemp()) { //чтение успешно
      Temp = ds.getTemp(); //записать значение
    }
  }
  Voltage = ina.getVoltage(); //записать значение напряжения 
  ShuntVoltage = ina.getShuntVoltage(); //записать значение напряжения на шунте
  if (sensor_Traction.available()) { //если готово
    Traction = sensor_Traction.read(); //записать значение тяги
  }
  if (sensor_Weight_1.available()) {
    Weight_1 = sensor_Weight_1.read();
  }
  if (sensor_Weight_2.available()) {
    Weight_2 = sensor_Weight_2.read();
  }

  if (millis() - time > 15) {
    control.writeMicroseconds(gas); //передать скорость мотора в регулятор 
  }

  if (Serial.available() > 1) { // Проверка наличия данных для парсинга
    char key = Serial.read(); // Чтение команды

    // Вывод команды для отладки
    Serial.print("Получена команда: ");
    Serial.println(key);

    // Проверка, является ли ключ допустимым
    if (key == 'm' || key == 'x' || key == 'g' || key == 'k' || key == 't') {
        String bufStr = Serial.readStringUntil('\n'); // Чтение всей строки до конца (до нового перевода строки)
        
        // Вывод строки для отладки
        Serial.print("Получена строка: ");
        Serial.println(bufStr);

        // Преобразуем строку в число
        int buf = bufStr.toInt();

        // Выводим полученное число для отладки
        Serial.print("Получено значение: ");
        Serial.println(buf);

        // Фильтрация некорректных данных по значению
        if (buf >= 0 && buf <= 3000) { // Проверка, что значение в допустимом диапазоне
            switch (key) {
                case 'm':
                    gas_min = buf;
                    EEPROM.put(0, gas_min); 
                    Serial.println("Изменен gas_min");
                    break;

                case 'x':
                    gas_max = buf;
                    EEPROM.put(3, gas_max); 
                    Serial.println("Изменен gas_max");
                    break;

                case 'g':
                    gas = buf;
                    control.writeMicroseconds(gas); // Передача значения скорости на мотор
                    step += 1;
                    Serial.print("сумма: ");
                    Serial.println(step);
                    break;

                case 'k':
                    EEPROM.get(0, gas_min); 
                    EEPROM.get(3, gas_max);
                    control.writeMicroseconds(gas_max); // Калибровка
                    delay(2000);
                    control.writeMicroseconds(gas_min);
                    delay(6000);
                    Serial.println("Калибровка завершена");
                    break;

                case 't': // Сброс таймера
                    Time = millis(); 
                    Serial.println("Таймер сброшен");
                    break;
            }
        } else {
            // Вывод сообщения об ошибке, если значение за пределами диапазона
            Serial.println("Ошибка: некорректное значение.");
        }
    } else {
        // Вывод сообщения об ошибке, если символ не распознан
        Serial.println("Ошибка: некорректная команда.");
    }
  }
  mainTime = millis() - Time; //счет таймера 

  Serial.print(T_flash_E); Serial.print(","); //отправка данных на ПК
  Serial.print(T_flash_O); Serial.print(",");
  Serial.print(Voltage, 3); Serial.print(",");
  Serial.print(ShuntVoltage, 3); Serial.print(",");
  Serial.print(Temp, 2); Serial.print(",");
  Serial.print(Traction, 1); Serial.print(",");
  Serial.print(Weight_1, 1); Serial.print(",");
  Serial.print(Weight_2, 1); Serial.print(",");
  Serial.print(mainTime); Serial.println(";");
}
 
void E_counter_RPM() {
  T_flash_E = micros() - lastflash_E; // время между двумя оборотами 
  lastflash_E = micros(); // время последнего оборота
}

void O_counter_RPM() {
  T_flash_O = micros() - lastflash_O; // время между двумя оборотами 
  lastflash_O = micros(); // время последнего оборота
}
