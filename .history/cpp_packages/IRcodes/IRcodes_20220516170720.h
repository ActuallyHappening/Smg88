#include <Arduino.h>

#ifdef IRCODES_INCLUDE_CANDLE
Serial.println(F("Including IRCodes::Candle"));
#include "IRcodes_Candle.h"
class IRcodes
{
  IRcodes_candle = IRcodes_Candle::Commands;
#else
#warning NOT including IRCODES_INCLUDE_CANDLE
#endif