#include <Arduino.h>

class CA_Command
{
public:
  int command;
  // bool matches(int address, int command)
  // {
  //   return (this->address == address) && (this->command == command);
  // }
  Command()
  {
    command = 0;
  }
  Command(int _command)
  {
    command = _command;
  }
};