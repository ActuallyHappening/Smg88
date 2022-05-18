#include <Arduino.h>

class Command
{
public:
  int address;
  int command;
  bool matches(int address, int command)
  {
    return (this->address == address) && (this->command == command);
  }
  Command()
  {
    address = 0;
    command = 0;
  }
  Command(int a, int c)
  {
    address = a;
    command = c;
  }
};

class IRcodes_Candle
{
public:
  Command ON;
  Command OFF;
  IRcodes_Candle()
  {
    ON = Command(0x80, 0x12);
    OFF = Command(0x80, 0x1A);
  }
} IRcodes_Candle;
