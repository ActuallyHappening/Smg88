#include <Smg88.h>
#include <IRremote.h>
#include <IRcodes.h>

#define DEBUG
#define INFO
//#define IMPLEMENTATION

// int shouldNOTERROR = testVar2;

#include "Smg88_localConfig.h"

AdafruitIO_Feed *Smg88_feed = io.feed("smg88-iot-management.iotm-ir-input");

void setup()
{
  Serial.begin(115200);
  Serial.println("Smg88 vm0.1.1"); // SCAN VERSION
  IrReceiver.begin(IR_RECEIVER_PIN, LED_BUILTIN);
  IrSender.begin(IR_SEND_PIN);

  Serial.print(F("Ready to receive IR signals of protocols: "));
  printActiveIRProtocols(&Serial);
  Serial.print(F("at pin "));
  Serial.println(IR_RECEIVER_PIN);

  io.connect();

  while (io.status() < AIO_CONNECTED)
  {
    Serial.print(F(". "));
    delay(420);
  }

  Serial.println();
  Serial.println(io.statusText());
}

void loop()
{
#ifdef IMPLEMENTATION
  Serial.println(F("Looping ..."));
#endif
  io.run();
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
    Serial.println(F("Known protocol"));
    if (myProtocol & decode_type_t::NEC)
    {
      Serial.println(F("NEC protocol yes!"));
      if (myAddress == IRcodes.Candle.address)
      {
        if (myCommand == IRcodes.Candle.ON.command)
        {
          Serial.println(F("ON -> Sending to Feed"));
          Smg88_feed->save("ESP32 IRcodes version = " + String(IRCODES_VERSION) + " = ON");
        }
        else if (myCommand == IRcodes.Candle.OFF.command)
        {
          Serial.println(F("OFF -> Sending to Feed"));
          Smg88_feed->save("ESP32 IRcodes version = " + String(IRCODES_VERSION) + " = ON");
        }
        else
        {
          Serial.println("Unknown command, myAddress = " + String(myAddress) + ", myCommand = " + String(myCommand));
          Serial.println("Wanted Address: " + String(IRcodes.Candle.address) + ", Wanted Command: " + String(IRcodes.Candle.ON.command));
        }
      }
      else
      {
        Serial.println(F("Unknown address"));
      }
    }
    else
    {
      Serial.println(F("Protocol not programmed for :("));
    }
  }
}
