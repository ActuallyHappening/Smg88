#include "Smg88.h"
#include "IRcodes.h"

using namespace Smg88; // Their is a class inside Smg88.h so using the file namespace to access the class (more intuitive)

String
Smg88::IRhandler::handleIRSection(uint_16 myCommandRaw)
{
}

String Smg88::IRhandler::handleIRGroup(decode_type_t myProtocol, uint_16 myAddress, uint_16 myCommand)
{
  String myResult = "__default__";
  return myResult;
}

String Smg88::IRhandler::handleIRGroup(IRData inputData)
{
  decode_type_t myProtocol = inputData.protocol;
  uint_16 myCommand = inputData.command;
  uint_16 myAddress = inputData.address;
  return Smg88::IRhandler::handleIRGroup(myProtocol, myAddress, myCommand);
}