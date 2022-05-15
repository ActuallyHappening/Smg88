#include "Smg88.h"

String HandleIRGroup(IRData inputData)
{
  String myResult = "";
  decode_type_t myProtocol = inputData.protocol;
  uint_16 myCommand = inputData.command;
  uint_16 myAddress = inputData.address;
  if (myProtocol & decode_type_t::UNKNOWN)
  {
    myResult = "Unknown protocol";
  }
  else
  {
    ;
  }
}