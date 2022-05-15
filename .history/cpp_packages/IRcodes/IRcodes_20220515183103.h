#include <IRremote.h>

struct action
{
  int command;
  void send();
};

struct candleLightIntegration
{
  int address;
  action ON;
};