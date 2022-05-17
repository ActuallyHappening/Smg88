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
  IRcodes_Candle()
  {
    ON = Command(0x80, 0x12); // TODO don't think this is a int literal WTF ??
    OFF = Command(0x80, 0x1A);
  }
} IRcodes_Candle_Commands;