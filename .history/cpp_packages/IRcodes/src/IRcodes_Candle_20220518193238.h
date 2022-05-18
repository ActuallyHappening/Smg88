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
    CA_Command ON(18);
    CA_Command OFF(26);
  }
};