"""Enables my python scripts to communicate between running instances and to read secrets from pre-set physical files
"""
from enum import Enum, auto
import os
from pprint import pprint
from loghelp import EnumParent
import errors
import yaml
import platform as osplatform

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
            match osplatform.system():
                case "Linux":
                    self.platform = PlatformType.Linux
                case "Windows":
                    self.platform = PlatformType.Windows
                case _:
                    raise CommConfigurationError(
                        f"Unsupported platform :( {osplatform.system()}")
        else:
            self.platform = platform
        print(
            f"New PlatformInfo object created for {self.platform=}, {self.config=}")
        # Sets other stuff specific to the platform through properties

    class _getYAMLConfig(getLocation):
        def __init__(self, relativeLocation: str = CONFIG_RELATIVE_LOCATION) -> None:
            absLocation = os.path.join(
                os.path.dirname(__file__), relativeLocation)
            super().__init__(location=absLocation, locationType="file:text/yaml")

    @property
    def config(self):
        return self._getYAMLConfig(CONFIG_RELATIVE_LOCATION)

    def requestSecrets(self):
        """Returns a dictionary of secrets for that platform specifically
        """
        with self.config as config:
            try:
                configSpot = config["coms"]["platformInfo"][self.platform.value]["requestSecret"]
                location = getLocation(
                    location=configSpot["location"], locationType=configSpot["locationType"])
                return location
            except errors.Error as err:
                raise CommunicationError(err)


class Communicator():
    """Is responsible, and the 'API', for communicating from thread/process/project across platforms
    """

    def __init__(self, platformInfo: PlatformInfo = NONE) -> None:
        if platformInfo is NONE:
            self.platformInfo = PlatformInfo()
        else:
            self.platformInfo = platformInfo

    @property
    def platform(self) -> PlatformInfo:
        return self.platformInfo.platform

    def requestSecret(self, secretHandle: str):
        """Returns the secret associated with the secretHandle
        """
        recursivePath = secretHandle.split(" ")
        with self.platformInfo.requestSecrets() as secrets:
            try:
                for path in recursivePath:
                    secrets = secrets[path]
                secret = secrets  # For clarity, as the recursive path leads to a singular secret
                return secret
            except (KeyError, errors.Error) as err:
                raise CommSecretExtractionError(err)


if __name__ == "__main__":
    platformInfo = PlatformInfo()
    comm = Communicator(platformInfo=platformInfo)
    testSecret = comm.requestSecret('ryanpinger TOKEN')
    print(f"{testSecret=}")
    with testSecret as secrets:
        print(f"{secrets=}")
