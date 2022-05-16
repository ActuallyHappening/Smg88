#include <Arduino.h>
#include <IRremote.h>

struct Command
{
  int address;
  int command;
}