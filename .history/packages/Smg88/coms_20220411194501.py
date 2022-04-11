"""Enables my python scripts to communicate between running instances and to read secrets from pre-set physical files
"""
from enum import Enum, auto
import os
from pprint import pprint
from loghelp import EnumParent
import errors
import yaml
import platform

NONE = object()  # Sentinel value for when a value is not found
# Exporting to the config file is counter-intuitive :)
CONFIG_RELATIVE_LOCATION = "config.yaml"


class CommunicationError(errors.Error):
    """Raised when there is an error in communication module (root class)
    """
    pass


class CommSecretExtractionError(CommunicationError):
    """Raised when there is an error in extracting secrets
    """
    pass


class CommConfigurationError(CommunicationError):
    """Raised when there is an error in opening / parsing a configuration file
    """
    pass


class PlatformType(EnumParent):
    Windows = auto()
    Linux = auto()


class getLocation():
    def __init__(self, location: str, locationType: str = "file:text/yaml"):
        self.locationType = locationType
        if location is NONE or type(location) is not str or location is None:
            raise errors.InappropriateRequest("location must be a string")
        else:
            self.location = location

    def __call__(self):
        match self.locationType.split(":"):
            case ("file", mimes):
                # Handle files as the location (with open)
                try:
                    self.file = open(self.location, "r")
                    match mimes.split("/"):
                        case ("text", "yaml"):
                            try:
                                # Errors shouldn't propagate
                                return yaml.safe_load(self.file)
                            except yaml.YAMLError as err:
                                # print(f"{err=}")
                                raise CommunicationError(err)
                        case _:
                            raise CommunicationError(
                                f"Unsupported file type: {mimes=}")
                except errors.Error as err:
                    # Propagate error with proper encapsulation of error types
                    raise CommunicationError(err)
            case _:
                raise CommunicationError(
                    f"Unsupported location type: {self.locationType=}")

    def __enter__(self):
        return self()

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


class getYAMLConfig(getLocation):
    def __init__(self, location: str =)


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
                    raise CommConfigurationError(
                        f"Unsupported platform :( {platform.system()}")
        else:
            self.platform = platform
        # Sets other stuff specific to the platform through properties

    def requestSecrets(self):
        if self.platform == PlatformType.Linux:

        elif self.platform == PlatformType.Windows:

        else:
            raise CommSecretExtractionError(
                f"Unsupported platform :( {self.platform.system()}")


class Communicator():
    def __init__(self, platformInfo: PlatformInfo = NONE, platform: PlatformType = NONE) -> None:
        if platformInfo is NONE:
            if platform is NONE:
                self.platformInfo = PlatformInfo()
                self.platform = self.platformInfo.platform
            else:
                self.platformInfo = PlatformInfo(platform=platform)
                self.platform = self.platformInfo.platform
        else:
            self.platformInfo = platformInfo
            self.platform = platformInfo.platform

    def requestSecret(self, secretHandle: str):
        """Returns the secret associated with the secretHandle
        """
        match secretHandle:
            case "ryanpinger TOKEN":
                return self.platformInfo.requestSecrets()["ryanpinger TOKEN"]


"""
if __name__ == "__main__":
  config = getYAMLConfig()
  print(f"{config.file=}")
  with config as configs:
    print(f"{configs=}")
"""
