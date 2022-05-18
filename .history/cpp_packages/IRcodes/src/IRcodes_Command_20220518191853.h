#include <Arduino.h>

class CA_Command
{
public:
  // int address;
  int command;
  // bool matches(int address, int command)
  // {
  //   return (this->address == address) && (this->command == command);
  // }
  Command()
  {
    // address = 0;
    command = 0;
  }
  Command(int a /*, int c*/)
  {
    // address = a;
    command = c;
  }
};