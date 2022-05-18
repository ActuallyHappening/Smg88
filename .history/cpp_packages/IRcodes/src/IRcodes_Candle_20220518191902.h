#include <Arduino.h>
#include "IRcodes_Command.h"

class IRCodes_Candle
{
public:
  int addredd = 0x80;
  CA_Command ON;
  CA_Command OFF;
  IRCodes_Candle()
  {
    ON = CA_Command(0x12);
    OFF = CA_Command(0x1A);
  }
};