#include <Arduino.h>

struct Command
{
  int address;
  int command;
}

class Commands
{
public:
  Command ON;
  Command OFF;
}