#include <Arduino.h>

#ifdef IRCODES_INCLUDE_CANDLE
#ifdef DEBUG
Serial.println(F("Including IRCodes::Candle"));
#endif

#include "IRcodes_Candle.h"

Candle = IRcodes_Candle::Commands;

#else
#warning NOT including IRCODES_INCLUDE_CANDLE
#endif