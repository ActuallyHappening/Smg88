#include <Smg88.h>
#include <IRremote.h>
#include <IRcodes.h>

#define IR_RECEIVER_PIN 13
#define IR_SEND_PIN 14

#define DEBUG
//#define INFO

void setup()
{
  Serial.begin(115200);
  Serial.println("Smg88");
  IrReceiver.begin(IR_RECEIVER_PIN, LED_BUILTIN);
  IrSender.begin(IR_SEND_PIN);
}

void loop()
{
#ifdef INFO
  Serial.println(F("Looping"));
#endif
}