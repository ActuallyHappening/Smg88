#include <Arduino.h>
#include "IRcodes_Command.h"

class IRCodes_Candle
{
public:
  int address = 0x80;
  CA_Command ON;
  CA_Command OFF;
  IRCodes_Candle()
  {
    CA_Command ON(0x12);
    CA_Command OFF(0x1A);
  }
};