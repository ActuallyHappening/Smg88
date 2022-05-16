#warning IRcodes.h Version 0.1.13 // SCAN VERSION
#define IRCODES_VERSION "0.1.13" // SCAN VERSION

#include <Arduino.h>

int testVar2 = 69420;

#ifdef IRCODES_INCLUDE_CANDLE
#ifdef DEBUG
Serial.println(F("Including IRCodes::Candle"));
#endif

#include "IRcodes_Candle.h"

class IRCodes
{
  Candle = IRcodes_Candle::Commands;
} IRcodes;

int test = 69;
#else
#warning NOT including IRCODES_INCLUDE_CANDLE
#endif
