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
    def __init__(self, /, location: str, *, locationType: str = "file:text/yaml"):
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


class PlatformInfo():
    """Is responsible for platform specific tasks, such as retrieving secrets (absolute locations will differ between platform types) and config files

    requestSecrets(secretHandle: str) -> str
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
        print(
            f"New PlatformInfo object created for {self.platform=}, {self.config=}s")
        # Sets other stuff specific to the platform through properties

    class _getYAMLConfig(getLocation):
      def __init__(self, relativeLocation: str = CONFIG_RELATIVE_LOCATION) -> None:
          absLocation = os.path.join(os.path.dir(__file__), relativeLocation)
          super().__init__(location=absLocation, locationType="file:text/yaml")

    @property
    def config(self):
      return self._getYAMLConfig(CONFIG_RELATIVE_LOCATION)

    def requestSecrets(self):
      """Returns a dictionary of secrets for that platform specifically
      """


class Communicator():
    """Is responsible, and the 'API', for communicating from thread/process/project across platforms
    """

    def __init__(self, platformInfo: PlatformInfo = NONE) -> None:
        if platformInfo is NONE:
            self.platformInfo = PlatformInfo()
        else:
            self.platformInfo = platformInfo

    @property
    def platformInfo(self) -> PlatformInfo:
      return self.platformInfo.platform

    def requestSecret(self, secretHandle: str):
        """Returns the secret associated with the secretHandle
        """
        match secretHandle:
            case "ryanpinger TOKEN":
                return self.platformInfo.requestSecrets()["ryanpinger TOKEN"]


if __name__ == "__main__":
  comm = Communicator()
