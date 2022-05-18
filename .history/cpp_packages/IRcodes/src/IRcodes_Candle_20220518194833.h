#include <Arduino.h>
#include "IRcodes_Command.h"

class IRCodes_Candle
{
public:
  int address = 128;
  CA_Command ON(0x12);
  CA_Command OFF(0x1A);
  IRCodes_Candle()
  {
  }
};