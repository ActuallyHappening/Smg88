/*
 *  PinDefinitionsAndMore.h
 *
 *  Contains pin definitions for IRremote examples for various platforms
 *  as well as definitions for feedback LED and tone() and includes
 *
 *  Copyright (C) 2021-2022  Armin Joachimsmeyer
 *  armin.joachimsmeyer@gmail.com
 *
 *  This file is part of IRremote https://github.com/Arduino-IRremote/Arduino-IRremote.
 *
 *  Arduino-IRremote is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/gpl.html>.
 *
 */

/*
 * Pin mapping table for different platforms
 *
 * Platform     IR input    IR output   Tone      Core/Pin schema
 * --------------------------------------------------------------
 * DEFAULT/AVR  2           3           4
 * ATtinyX5     0|PB0       4|PB4       3|PB3
 * ATtiny167    3|PA3       2|PA2       7|PA7     ATTinyCore
 * ATtiny167    9|PA3       8|PA2       5|PA7     Digispark pro
 * ATtiny3217  18|PA1      19|PA2      20|PA3     MegaTinyCore
 * ATtiny1604   2           3|PA5       %
 * SAMD21       3           4           5
 * ESP8266      14|D5       12|D6       %
 * ESP32        15          4           27
 * BluePill     PA6         PA7         PA3
 * APOLLO3      11          12          5
 * RP2040       3|GPIO15    4|GPIO16    5|GPIO17
 */

#define USE_TONE false // My own pre-processor directive (cool name!)

//#define _IR_MEASURE_TIMING // For debugging purposes.

/*
 * We do not have pin restrictions for this CPU's, so lets use the hardware PWM for send carrier signal generation
 */

#define SEND_PWM_BY_TIMER

#include <Arduino.h>

#define TONE_LEDC_CHANNEL 1 // Using channel 1 makes tone() independent of receiving timer -> No need to stop receiving timer.
void tone(uint8_t _pin, unsigned int frequency)
{
  ledcAttachPin(_pin, TONE_LEDC_CHANNEL);
  ledcWriteTone(TONE_LEDC_CHANNEL, frequency);
}
void tone(uint8_t _pin, unsigned int frequency, unsigned long duration)
{
  ledcAttachPin(_pin, TONE_LEDC_CHANNEL);
  ledcWriteTone(TONE_LEDC_CHANNEL, frequency);
  delay(duration);
  ledcWriteTone(TONE_LEDC_CHANNEL, 0);
}
void noTone(uint8_t _pin)
{
  ledcWriteTone(TONE_LEDC_CHANNEL, 0);
}
#define IR_RECEIVE_PIN 15  // D15
#define IR_SEND_PIN 4      // D4
#define TONE_PIN 27        // D27 25 & 26 are DAC0 and 1
#define APPLICATION_PIN 16 // RX2 pin

#if !defined(FLASHEND)
#define FLASHEND 0xFFFF // Dummy value for platforms where FLASHEND is not defined
#endif
/*
 * Helper macro for getting a macro definition as string
 */
#if !defined(STR_HELPER)
#define STR_HELPER(x) #x
#define STR(x) STR_HELPER(x)
#endif
