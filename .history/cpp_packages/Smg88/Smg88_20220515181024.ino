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
  Serial.println("Smg88");
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
      IrReceiver.printIRResultShort(&Serial);
      IRData myData = IrReceiver.decodedIRData;
      handleIRInput(myData);
    }
  }
  else
  {
#ifdef INFO
    Serial.println(F("No IR signal received"));
  }
}
void handleIRInput(IRData givenData)
{
  int myProtocol = givenData.protocol;
  if (myProtocol & IR_PROTOCOL_UNKNOWN)
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