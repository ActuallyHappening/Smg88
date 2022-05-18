#include <Arduino.h>

class CA_Command
{
public:
  int command;
  // bool matches(int address, int command)
  // {
  //   return (this->address == address) && (this->command == command);
  // }
  CA_Command()
  {
    command = 0;
  }
  CA_Command(int _command)
  {
    command = _command;
  }
};