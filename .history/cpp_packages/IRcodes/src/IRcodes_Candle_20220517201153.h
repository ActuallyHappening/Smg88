#include <Arduino.h>

struct Command
{
  int address;
  int command;
  bool matches(int address, int command)
  {
    return (this->address == address) && (this->command == command);
  }
  Command(int _address, int _command)
  {
    address = _address;
    command = _command;
  }
};

class IRcodes_Candle
{
public:
  Command ON;
  Command OFF;
} IRcodes_Candle_Commands;