#include <Arduino.h>

struct Command
{
  int address;
  int command;
  bool matches(int address, int command)
  {
    return (this->address == address) && (this->command == command);
  }
  Command(int address, int command)
  {
  }
};

class IRcodes_Candle_Commands
{
public:
  Command ON;
  Command OFF;
};