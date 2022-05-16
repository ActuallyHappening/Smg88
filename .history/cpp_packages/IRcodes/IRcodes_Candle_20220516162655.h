#include <Arduino.h>
#include <IRremote.h>

#ifdef INFO
Serial.println(F("Running IRCodes::Candle"));
#endif

#ifdef IRCODES_INCLUDE_CANDLE

#ifdef IRCODES_INCLUDE_CANDLE_STRICT
// Only include specific candle commands
#ifdef DEBUG
Serial.println(F("Including IRCodes::Candle::Strict"));
#endif

#ifdef IR_CODES_INCLUDE_CANDLE_COMMAND_ON
String Command_On()
{
  IrReceiver.sendNEC(0x0, 0x3, 3);
}
#endif

#else
// Include all candle commands except
#ifdef DEBUG
Serial.println(F("Including IRCodes::Candle::All"));
#endif

#endif
#else
#ifdef DEBUG
Serial.println(F("Not Loading Candles (although script ran)"))
#endif
#endif