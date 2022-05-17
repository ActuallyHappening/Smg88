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

class IRcodes_Candle
{
public:
  Command ON;
  Command OFF;
};