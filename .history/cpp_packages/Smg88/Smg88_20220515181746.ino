#include <Smg88.h>
#include <IRremote.h>
#include <IRcodes.h>

#define IR_RECEIVER_PIN 13
#define IR_SEND_PIN 14

#define DEBUG
//#define INFO

void setup()
{
  Serial.begin(115200);
  Serial.println("Smg88 v0.0.0");
  IrReceiver.begin(IR_RECEIVER_PIN, LED_BUILTIN);
  IrSender.begin(IR_SEND_PIN);

  Serial.print(F("Ready to receive IR signals of protocols: "));
  printActiveIRProtocols(&Serial);
  Serial.print(F("at pin "));
  Serial.println(IR_RECEIVE_PIN);
}

void loop()
{
#ifdef INFO
  Serial.println(F("Looping ..."));
#endif
  if (IrReceiver.decode())
  {
    if (IrReceiver.decodedIRData.flags & IRDATA_FLAGS_WAS_OVERFLOW)
    {
      Serial.println(F("Overflow detected! Probably to complicated an IR signal (like AirCon controller)"));
      Serial.println(F("Try to increase the \"RAW_BUFFER_LENGTH\" value of " STR(RAW_BUFFER_LENGTH) " in " __FILE__));
    }
    else
    {
      // Print a short summary of received data
      Serial.print(F("Received IR data:"));
      IrReceiver.printIRResultShort(&Serial);
      Serial.println();
      IRData myData = IrReceiver.decodedIRData;
      handleIRInput(myData);
      IrReceiver.resume();
    }
  }
  else
  {
    ;
#ifdef INFO
    Serial.println(F("No IR signal received"));
#endif
  }
}
void handleIRInput(IRData givenData)
{
  decode_type_t myProtocol = givenData.protocol;
  if (myProtocol & decode_type_t.UNKNOWN)
  {
    Serial.println(F("Unknown protocol"));
  }
  else
  {
    Serial.print(F("Protocol: "));
    Serial.println(myProtocol);
    Serial.print(F("Command: "));
    Serial.println(givenData.command);
    Serial.print(F("Address: "));
    Serial.println(givenData.address);
    Serial.print(F("Raw data: "));
  }
}