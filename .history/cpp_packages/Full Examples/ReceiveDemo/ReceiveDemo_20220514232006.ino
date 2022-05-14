/*
 * ReceiveDemo.cpp
 *
 * Demonstrates receiving IR codes with the IRremote library.
 * If debug button is pressed (pin connected to ground) a long output is generated.
 *
 *  This file is part of Arduino-IRremote https://github.com/Arduino-IRremote/Arduino-IRremote.
 *
 ************************************************************************************
 * MIT License
 *
 * Copyright (c) 2020-2022 Armin Joachimsmeyer
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is furnished
 * to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
 * PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
 * CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
 * OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 ************************************************************************************
 */

#include <Arduino.h>

/*
 * Specify which protocol(s) should be used for decoding.
 * If no protocol is defined, all protocols are active.
 * This must be done before the #include <IRremote.hpp>
 */
//#define DECODE_LG
//#define DECODE_NEC
// etc. see IRremote.hpp
#define NEC

#define EXCLUDE_EXOTIC_PROTOCOLS
#define EXCLUDE_UNIVERSAL_PROTOCOLS // Saves up to 1000 bytes program space.

//#define DEBUG // Activate this for lots of lovely debug output from the decoders.
#define INFO // To see valuable informations from universal decoder for pulse width or pulse distance protocols
/*
 * First define macros for input and output pin etc.
 */
#include "PinDefinitionsAndMore.h"
#include <IRremote.hpp>

#if defined(APPLICATION_PIN)
#define DEBUG_BUTTON_PIN APPLICATION_PIN // if low, print timing for each received data set
#else
#define DEBUG_BUTTON_PIN 6
#endif

void setup()
{
  Serial.begin(115200);

  // Just to know which program is running on my Arduino
  Serial.println(F("START " __FILE__ " from " __DATE__));
  Serial.println(F("Using library version " VERSION_IRREMOTE));

  // In case the interrupt driver crashes on setup, give a clue
  // to the user what's going on.
  Serial.println(F("Enabling IRin..."));

  // Start the receiver and if not 3. parameter specified, take LED_BUILTIN pin from the internal boards definition as default feedback LED
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);

  Serial.print(F("Ready to receive IR signals of protocols: "));
  printActiveIRProtocols(&Serial);
  Serial.print(F("at pin "));

  Serial.println(IR_RECEIVE_PIN);

#if FLASHEND >= 0x3FFF // For 16k flash or more, like ATtiny1604. Code does not fit in program space of ATtiny85 etc.
  Serial.print(F("Debug button pin is "));
  Serial.println(DEBUG_BUTTON_PIN);

  // infos for receive
  Serial.print(RECORD_GAP_MICROS);
  Serial.println(F(" us is the (minimum) gap, after which the start of a new IR packet is assumed"));
  Serial.print(MARK_EXCESS_MICROS);
  Serial.println(F(" us are subtracted from all marks and added to all spaces for decoding"));
#endif
}

void loop()
{
  /*
   * Check if received data is available and if yes, try to decode it.
   * Decoded result is in the IrReceiver.decodedIRData structure.
   *
   * E.g. command is in IrReceiver.decodedIRData.command
   * address is in command is in IrReceiver.decodedIRData.address
   * and up to 32 bit raw data in IrReceiver.decodedIRData.decodedRawData
   */
  if (IrReceiver.decode())
  {
    Serial.println();
#if FLASHEND >= 0x3FFF // For 16k flash or more, like ATtiny1604
    if (IrReceiver.decodedIRData.flags & IRDATA_FLAGS_WAS_OVERFLOW)
    {
      Serial.println(F("Overflow detected"));
      Serial.println(F("Try to increase the \"RAW_BUFFER_LENGTH\" value of " STR(RAW_BUFFER_LENGTH) " in " __FILE__));
      // see also https://github.com/Arduino-IRremote/Arduino-IRremote#modifying-compile-options-with-sloeber-ide
#if !defined(ESP8266) && !defined(NRF5)
      /*
       * do double beep
       */
#if !defined(ESP32)
      IrReceiver.stop(); // ESP32 uses another timer for tone()
#endif
      tone(TONE_PIN, 1100, 10);
      delay(50);
      tone(TONE_PIN, 1100, 10);
      delay(50);
#if !defined(ESP32)
      IrReceiver.start(100000); // to compensate for 100 ms stop of receiver. This enables a correct gap measurement.
#endif
#endif
    }
    else
    {
      // Print a short summary of received data
      IrReceiver.printIRResultShort(&Serial);

      if (IrReceiver.decodedIRData.protocol == UNKNOWN || digitalRead(DEBUG_BUTTON_PIN) == LOW)
      {
        // We have an unknown protocol, print more info
        IrReceiver.printIRResultRawFormatted(&Serial, true);
      }
    }

    // tone on esp8266 works once, then it disables the successful IrReceiver.start() / timerConfigForReceive().
    if (IrReceiver.decodedIRData.protocol != UNKNOWN)
    {
      /*
       * If a valid protocol was received, play tone, wait and restore IR timer.
       * Otherwise do not play a tone to get exact gap time between transmissions.
       * This will give the next CheckForRecordGapsMicros() call a chance to eventually propose a change of the current RECORD_GAP_MICROS value.
       */
      tone(TONE_PIN, 2200, 8);
      delay(8);
      IrReceiver.start(8000); // to compensate for 8 ms stop of receiver. This enables a correct gap measurement.
    }
#endif // FLASHEND

    /*
     * !!!Important!!! Enable receiving of the next value,
     * since receiving has stopped after the end of the current received data packet.
     */
    IrReceiver.resume();

    /*
     * Finally check the received data and perform actions according to the received address and commands
     */
    if (IrReceiver.decodedIRData.address == 0)
    {
      if (IrReceiver.decodedIRData.command == 0x10)
      {
        // do something
      }
      else if (IrReceiver.decodedIRData.command == 0x11)
      {
        // do something else
      }
    }
  } // if (IrReceiver.decode())

  /*
   * Your code here
   * For all users of the FastLed library, use this code for strip.show() to improve receiving performance (which is still not 100%):
   * if (IrReceiver.isIdle()) {
   *     strip.show();
   * }
   */
}
