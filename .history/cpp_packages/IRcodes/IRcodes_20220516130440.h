#include <Arduino.h>
#include "IRremote.h"
class IRcodes
{
public:
  struct Data
  {
    __raw__
        decode_type_t protocol;
    uint_16 command;
    uint_16 address;
    void send(uint_16 myIrSender);
    void is(IRData checkData);
  } struct Section
  {
    Data __raw__;
    uint_16 command;
  }

  class DATA
  {
    Data ON;
    Data OFF;
  }
}