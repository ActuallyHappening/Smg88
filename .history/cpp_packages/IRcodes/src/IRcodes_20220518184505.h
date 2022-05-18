#warning IRcodes.h Version 0.1.31 // SCAN VERSION
#define IRCODES_VERSION "0.1.31" // SCAN VERSION

#include <Arduino.h>
#define IRCODES_INCLUDE_CANDLE

class

#ifdef IRCODES_INCLUDE_CANDLE
#ifdef DEBUG
    Serial.println(F("Including IRCodes::Candle version " IRCODES_VERSION));
#endif

#include "IRcodes_Candle.h"

class IRCodes
{
public:
  IRCodes_Candle Candle;
  IRCodes()
  {
    Candle = IRcodes_Candle;
  }
} IRcodes;

#else
#warning NOT including IRCODES_INCLUDE_CANDLE
#endif
