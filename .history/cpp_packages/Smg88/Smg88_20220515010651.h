#define LED_BUILTIN 3
#define IR_RECEIVER_PIN 13
#define IR_SEND_PIN 14

#include <IRcodes.h>

void setup()
{
  Serial.begin(115200);
  Serial.println("Smg88");
}