#include <Arduino.h>
#include "IRremote.h"
class IRcodes
{
public:
  struct Data
  {
    IRData __raw__;
    decode_type_t protocol;
    uint_16 address;
    uint_16 command;
    void send(uint_16 myIrSender);
    void is(IRData checkData);
  } struct Group // Marks a subset of Data for constant protocols
  {
    Data __raw__;
    decode_type_t chosenProtocol;
    uint_16 address;
    uint_16 command;
    void send(uint_16 address, uint_16 command, uint_16 myIrSender);
  } struct Section
  {
    Group __raw__;
    decode_type_t chosenProtocol;
    uint_16 chosenAddress;
    uint_16 command;
    void send(uint_16 command, uint_16 myIrSender);
  }

  class DATA
  {
    Data ON;
    Data OFF;
  }
}