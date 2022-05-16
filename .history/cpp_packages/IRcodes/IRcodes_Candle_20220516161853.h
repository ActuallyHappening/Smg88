#include <Arduino.h>
#include <IRremote.h>

#ifdef INFO
#warning Running IRCodes::Candle
#endif

#ifdef IRCODES_INCLUDE_CANDLE

#ifdef IRCODES_INCLUDE_CANDLE_STRICT
// Only include specific candle commands

#else
#ifdef DEBUG
Serial.println

#else
#ifdef DEBUG
Serial.println(F("Not Loading Candles (although script ran)"))
#endif
#endif