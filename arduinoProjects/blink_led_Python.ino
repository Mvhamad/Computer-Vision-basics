#include <cvzone.h>

SerialData serialData(1,1);
int valRec[1];
void setup() {
  serialData.begin();
  pinMode(13,OUTPUT);

}

void loop() {
  serialData.Get(valRec);
  digitalWrite(13, valRec[0]);
}
