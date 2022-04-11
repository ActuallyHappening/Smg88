"""Enables my python scripts to communicate between running instances and to read secrets from pre-set physical files
"""
from enum import Enum, auto
from .loghelp import EnumParent
import yaml

NONE = object()  # Sentinel value for when a value is not found


class CommError(Exception):
  """Raised when there is an error in communication
  """
  pass


class SecretExtractionError(CommError):
  """Raised when there is an error in extracting secrets
  """
  pass


class CommConfigError(CommError):
  """Raised when there is an error in opening a configuration file
  """
  pass


class PlatformType(EnumParent):
  Windows = auto()
  Linux = auto()


class getYAML():
  def __init__(self) -> None:
    self.file = open("coms.yaml", "r")

  def __call__(self):
    try:
      info = yaml.load(self.file)
      print(info)
      return info
    except yaml.YAMLError as exc:
      print(exc)
      raise CommConfigError()

  def __enter__():
    return self.file

  def __exit__(self, exc_type, exc_value, exc_traceback):
    self.file.close()


class PlatformInfo():
  def __init__(self, platform=NONE) -> None:
    with open("coms.yaml", "r") as stream:
      try:
        print(yaml.safe_load(stream))
      except yaml.YAMLError as exc:
        print(exc)

class Communicator():
  def __init__(self, platform: PlatformType, platformInfo: PlatformInfo = NONE) -> None:
    self.platform = platform
    if platformInfo is not NONE:
      self.platformInfo = platformInfo
    else:
      self.platformInfo = PlatformInfo(self.platform)
  def requestSecret(secretHandle: str):
    """Returns the secret associated with the secretHandle
    """
    match secretHandle:
      case "ryanpinger TOKEN":
        return "to be inserted"
