#include <cvzone.h>

int red = 10;
int green = 9;
int blue = 8;

SerialData serialData(3,1);
int valRecs[3];

void setup() {
  serialData.begin();
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
}

void loop() {
  serialData.Get(valRecs);
  digitalWrite(red,valRecs[0]);
  digitalWrite(green,valRecs[2]);
  digitalWrite(blue,valRecs[1]);
  delay(1000);
}
