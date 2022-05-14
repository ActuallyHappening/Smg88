#define LED_BUILTIN 2

#include <Smg88.h>
#include <IRremote.h>
#include <IRcodes.h>

void setup()
{
  Serial.begin(115200);
  Serial.println("Smg88");
  IrReceiver.begin();
}