#warning IRcodes.h Version 0.1.31 // SCAN VERSION
#define IRCODES_VERSION "0.1.31" // SCAN VERSION

#include <Arduino.h>
#define IRCODES_INCLUDE_CANDLE

#ifdef IRCODES_INCLUDE_CANDLE
#ifdef DEBUG
Serial.println(F("Including IRCodes::Candle version " IRCODES_VERSION));
#endif

#include "IRcodes_Candle.h"

class IRCodes
{
  IRcodes_Candle_Commands Candle = IRcodes_Candle_Commands();
} IRcodes;

#else
#warning NOT including IRCODES_INCLUDE_CANDLE
#endif
