#include "Smg88.h"

String Smg88::IRhandler::handleIRGroup(decode_type_t myProtocol, uint_16 myAddress, uint_16 myCommand)
{
  String myResult = "";
}

String Smg88::IRhandler::handleIRGroup(IRData inputData)
{
  decode_type_t myProtocol = inputData.protocol;
  uint_16 myCommand = inputData.command;
  uint_16 myAddress = inputData.address;
  return Smg88::IRhandler::handleIRGroup(myProtocol, myAddress, myCommand);
}