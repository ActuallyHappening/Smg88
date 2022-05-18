#include <Arduino.h>

class test
{
public:
  int var1;
  test(int input)
  {
    var1 = input;
  }
}

void
setup()
{
  test myTest = test(69);
  Serial.println(myTest.var1);
}
void loop() {}