#include <Arduino.h>
#include "IRcodes_Command.h"

class IRCodes_Candle
{
public:
  Command ON;
  Command OFF;
  IRCodes_Candle()
  {
    ON = Command(0x80, 0x12);
    OFF = Command(0x80, 0x1A);
  }
} IRcodes_Candle;
