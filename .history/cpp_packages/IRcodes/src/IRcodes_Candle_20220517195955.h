#include <Arduino.h>

struct Command
{
  int address;
  int command;
  bool matches(int address, int command)
  {
    return (this->address == address) && (this->command == command);
  }
};

class IRcodes_Candle_Commands
{
  IRcodes_Candle_Commands(list commands)
  {
    this->commands = commands;
  }
};