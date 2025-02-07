#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Настраиваем LCD (адрес дисплея 0x27, 16 символов, 2 строки)
LiquidCrystal_I2C lcd(0x27, 16, 2);

unsigned long lastHighTime = 0;        // Время последнего состояния HIGH
unsigned long stateChangeDuration = 0; // Длительность между двумя HIGH
//bool waitingForLow = false;            // Флаг для отслеживания LOW состояния
bool is_check = false;
bool lastState = LOW;                  // Предыдущее состояние сигнала

#define RPM_PIN 3 // Пин для подключения щелевого датчика
long lastOutputTime = 0; // Время последнего вывода данных

void setup() {
  pinMode(RPM_PIN, INPUT);  // Настраиваем пин как вход
  Serial.begin(9600);       // Открываем последовательный порт для вывода данных

  // Инициализация LCD
  lcd.init();
  lcd.backlight(); // Включаем подсветку
  lcd.setCursor(0, 0);
  lcd.print("Waiting for");
  lcd.setCursor(0, 1);
  lcd.print("data...");
}

void loop() {
  // Считываем текущее состояние пина
  bool currentState = digitalRead(RPM_PIN);

  if(lastState != currentState){
    if (currentState == HIGH && is_check == false){
      is_check = true;
      lastHighTime = millis();
    }
    else if(currentState == HIGH && is_check == true){
      stateChangeDuration = millis() - lastHighTime;
      is_check = false;
    }
    lastState = currentState;
    outprint();
  }
}

void outprint(){
    // Выводим данные каждые 500 мс
  if (millis() - lastOutputTime >= 500) {
    lastOutputTime = millis(); // Обновляем время последнего вывода

    // Выводим данные в Serial Monitor
    Serial.print("Time between HIGHs = ");
    Serial.print(stateChangeDuration);
    Serial.println("ms");

    // Выводим данные на LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("RPM = "); lcd.print(TakeRpm(stateChangeDuration));
  }

}

int TakeRpm(unsigned int time_rpm)
{
  if (time_rpm != 0) 
  {
  return (60000 / time_rpm) ;
  }
}