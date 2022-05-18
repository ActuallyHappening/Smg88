#include <Arduino.h>
#include "IRcodes_Command.h"

class IRCodes_Candle
{
public:
  int address = 128;
  CA_Command ON;
  CA_Command OFF;
  IRCodes_Candle()
  {
    ON(18);
    OFF(26);
  }
};