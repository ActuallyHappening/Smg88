#include "Smg88.h"
#include <IRremote.hpp>
#include "IRcodes.h"

#define DEBUG
#define INFO
//#define IMPLEMENTATION

void setup()
{
  Serial.begin(115200);
  Serial.println("Smg88 v0.0.3");
  IrReceiver.begin(IR_RECEIVER_PIN, LED_BUILTIN);
  IrSender.begin(IR_SEND_PIN);

  Serial.print(F("Ready to receive IR signals of protocols: "));
  printActiveIRProtocols(&Serial);
  Serial.print(F("at pin "));
  Serial.println(IR_RECEIVER_PIN);
}

void loop()
{
#ifdef IMPLEMENTATION
  Serial.println(F("Looping ..."));
#endif
  if (IrReceiver.decode())
  {
    if (IrReceiver.decodedIRData.flags & IRDATA_FLAGS_WAS_OVERFLOW)
    {
      Serial.println(F("Overflow detected! Probably to complicated an IR signal (like AirCon controller)"));
      Serial.println("Try to increase the \"RAW_BUFFER_LENGTH\" value of " + String(RAW_BUFFER_LENGTH) + " in " + __FILE__);
    }
    else
    {
      // Print a short summary of received data
      Serial.print(F("Received IR data:"));
      IrReceiver.printIRResultShort(&Serial);
      Serial.println();
      IRData myData = IrReceiver.decodedIRData;
      handleIRInput(myData); // Handles data custom function
      IrReceiver.resume();
    }
  }
  else
  {
    ;
#ifdef IMPLEMENTATION
    Serial.println(F("No IR signal received"));
#endif
  }
}
void handleIRInput(IRData givenData)
{
  decode_type_t myProtocol = givenData.protocol;
  int myCommand = givenData.command;
  int myAddress = givenData.address;
  if (myProtocol & decode_type_t::UNKNOWN)
  {
    Serial.println(F("Unknown protocol"));
  }
  else
  {
    // Could do stuff here :)
    Serial.println(IRcodes);
    Serial.println(IRcodes::Candle);
    Serial.println(IRCodes::Candle.ON);
    if (IRcodes::Candle.ON.matches(myAddress, myCommand))
    {
      Serial.println(F("Received IR signal for ON"));
    }
    else
    {
      Serial.println(F("Unknown command :("));
    }
  }
}
