#include <Arduino.h>
#include "IRremote.h"
class IRcodes
{
public:
  struct Data
  {
    uint_16 command;
    uint_16 address;
    void send(uint_16 myIrSender);
    void is(IRData checkData);
  } class DATA
  {
    Data ON;
    Data OFF;
  }
}