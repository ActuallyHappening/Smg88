#include <Arduino.h>

#define LED_BUILTIN 2
#define IR_RECEIVER_PIN 13
#define IR_SEND_PIN 14

#include "IRcodes.h"
#include <IRremote.h>

class Smg88
{
public:
  class IRhandler
  {
  public:
    String handleIRGroup(IRData inputData);
    String handleIRGroup(decode_type_t myProtocol, uint_16 myAddress, uint_16 myCommand);
  }
}