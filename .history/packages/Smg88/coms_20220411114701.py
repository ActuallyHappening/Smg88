"""Enables my python scripts to communicate between running instances and to read secrets from pre-set physical files
"""
from enum import Enum, auto
from .loghelp import EnumParent
import yaml


class PlatformType(EnumParent):
  Windows = auto()
  Linux = auto()


class PlatformInfo():
  def __init__(self) -> None:
    with open("coms.yaml", "r") as stream:
      try:
        print(yaml.safe_load(stream))
      except yaml.YAMLError as exc:
        print(exc)


class CommError(Exception):
  """Raised when there is an error in communication
  """
  pass


class SecretExtractionError(CommError):
  """Raised when there is an error in extracting secrets
  """
  pass


class Communicator():
  def __init__(self, platform: PlatformType):
    self.platform = platform
  def requestSecret(secretHandle: str):
    """Returns the secret associated with the secretHandle
    """
    match secretHandle:
      case "ryanpinger TOKEN":
        return "to be inserted"
