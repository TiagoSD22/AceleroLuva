#include "AcceleroMMA7361.h"
#include <SoftwareSerial.h>
AcceleroMMA7361 accelero;
SoftwareSerial mySerial (8, 9); //RX,TX

int x;
int y;
int z;
char ultimo_caractere;
char ultimo_caractere_comando = 'x';
const int modo_HID = 4;
const int acao1 = 2;
const int acao2 = 3;
const int limite = 40;
int delay_acelerometro = 100;
int delay_botao = 50;
long lastDebounceTime = 0;
long lastDebounceTime2 = 0;
bool x_pressionado = false;
bool y_pressionado = false;
bool z_pressionado = false;
bool b1_pressionado = false;
bool b2_pressionado = false;

void setup()
{
  pinMode(modo_HID, INPUT);
  pinMode(acao1,INPUT);
  pinMode(acao2,INPUT);
  Serial.begin(9600);
  mySerial.begin(9600);
  accelero.begin(13, 12, 11, 10, A0, A1, A2);
  accelero.setARefVoltage(3.3);                   
  accelero.setSensitivity(LOW);                   
  accelero.calibrate();
  Configurar_Bluetooth();
}

void Configurar_Bluetooth() {
  delay(500);
  mySerial.print("AT+INQ\r\n");
  delay(10000);
  mySerial.print("AT+CONN1\r\n");
}

void Ler() {
  x = accelero.getXAccel();
  y = accelero.getYAccel();
  z = accelero.getZAccel();
  ultimo_caractere = 'x';
  if (abs(x) > abs(y)) {
    if (x > limite) {
      ultimo_caractere = 'd';
      delay(delay_acelerometro);
    }
    else {
      if (x < -(limite)) {
        ultimo_caractere = 'a';
        delay(delay_acelerometro);
      }
    }
  }
  else {
    if (y > limite) {
      ultimo_caractere = 's';
      delay(delay_acelerometro);
    }
    else if (y < -limite) {
      ultimo_caractere = 'w';
      delay(delay_acelerometro);
    }
  }
  if(z > 150){
    ultimo_caractere = 'p';
    delay(delay_acelerometro);
  }
  else if(z < -20){
    if(ultimo_caractere != 'b'){
      ultimo_caractere = 'b';
      delay(delay_acelerometro);
    }
    else{
      ultimo_caractere = 'x';
    }
  }
  if(ultimo_caractere != 'x'){
     mySerial.print(ultimo_caractere);
   }
  delay(100);
}

void Ler_HID() {
  x = accelero.getXAccel();
  y = accelero.getYAccel();
  z = accelero.getZAccel();
  ultimo_caractere = 'x';
  if (abs(x) > abs(y)) {
    if (x > limite) {
      x_pressionado = true;
      mySerial.print('d');
      delay(delay_acelerometro);
    }
    else {
      if (x < -(limite)) {
        x_pressionado = true;
        mySerial.print('a');
        delay(delay_acelerometro);
      }
      else{
        if(x_pressionado == true){
          mySerial.print('X');
          delay(delay_acelerometro);
        }
        x_pressionado = false;
      }
    }
  }
  else {
    if (y > limite) {
      y_pressionado = true;
      mySerial.print('s');
      delay(delay_acelerometro);
    }
    else {
      if (y < -(limite)) {
        y_pressionado = true;
        mySerial.print('w');
        delay(delay_acelerometro);
      }
      else{
        if(y_pressionado == true){
          mySerial.print('Y');
          delay(delay_acelerometro);
        }
        y_pressionado = false;
      }
    }
  }
  if(z > 0){
    ultimo_caractere_comando = 'x';
  }
  if(z > 150){
    mySerial.print('p');
    delay(delay_acelerometro);
  }
  else if(z < -20){
    if(ultimo_caractere_comando != 'b'){
      ultimo_caractere_comando = 'b';
      mySerial.print('b');
      delay(delay_acelerometro);
    }
  }
  if ( (millis() - lastDebounceTime) > delay_botao) {
      if (digitalRead(acao1) == HIGH) {
        b1_pressionado = true;
        mySerial.print('j');
        lastDebounceTime = millis();
      }
      else{
        if(b1_pressionado == true){
          b1_pressionado = false;
          mySerial.print('J');
        }
      }
    }
    if ( (millis() - lastDebounceTime2) > delay_botao) {
      if (digitalRead(acao2) == HIGH) {
        b2_pressionado = true;
        mySerial.print('k');
        lastDebounceTime2 = millis();
      }
      else{
        if(b2_pressionado == true){
          b2_pressionado = false;
          mySerial.print('K');
        }
      }
    }
  delay(100);
}

void loop(){
  if(digitalRead(modo_HID) == LOW){
    Ler();
  }
  else{
    Ler_HID();
  }
}
