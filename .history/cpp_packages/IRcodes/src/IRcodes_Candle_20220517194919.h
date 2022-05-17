#include <Arduino.h>

class IRcodes_Candle
{
  struct Command
  {
    int address;
    int command;
    bool matches(int address, int command)
    {
      return (this->address == address) && (this->command == command);
    }
  };

  class Commands
  {
  public:
    Command ON;
    Command OFF;
  };
}