#include <Arduino.h>

#ifdef IRCODES_INCLUDE_CANDLE
#ifdef DEBUG
Serial.println(F("Including IRCodes::Candle"));
#endif

#include "IRcodes_Candle.h"

class IRCodes
{
  Candle = IRcodes_Candle::Commands;
} IRcodes;

int __test__ = 69;
#else
#warning NOT including IRCODES_INCLUDE_CANDLE
#endif