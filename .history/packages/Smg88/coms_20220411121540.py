"""Enables my python scripts to communicate between running instances and to read secrets from pre-set physical files
"""
from enum import Enum, auto
from .loghelp import EnumParent
import yaml
import platform

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


class getYAMLConfig():
  def __init__(self, fileLocation="coms.yaml") -> None:
    self.file = open(fileLocation, "r")

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
  """Is responsible for platform specific tasks, such as retrieving secrets (absolute locations will differ between platform types)
  """

  def __init__(self, platform: PlatformType = NONE) -> None:
    if platform == NONE:
      # Find platform from module 'platform'
      match platform.system():
        case "Linux":
          self.platform = PlatformType.Linux
        case "Windows":
          self.platform = PlatformType.Windows
        case _:
          raise CommError(f"Unsupported platform :( {platform.system()}")
    else:
      self.platform = platform
    ...
    # Sets other stuff specific to the platform

class Communicator():
  def __init__(self, platformInfo: PlatformInfo = NONE, platform: PlatformType = NONE) -> None:
    if platformInfo is NONE:
      self.platformInfo = PlatformInfo()
      self.platform = self.platformInfo.platform
  def requestSecret(secretHandle: str):
    """Returns the secret associated with the secretHandle
    """
    match secretHandle:
      case "ryanpinger TOKEN":
        return "to be inserted"
