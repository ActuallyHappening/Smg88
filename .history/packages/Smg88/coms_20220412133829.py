"""Enables my python scripts to communicate between running instances and to read secrets from pre-set physical files
"""
from enum import auto
import os
from pprint import pprint
from typing import final, overload
from loghelp import EnumParent
import errors
from errors import ProgrammerErrorHandle, UserErrorHandle
import yaml
import platform as osplatform

FILE_NAME = os.path.basename(__file__)
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
class CommunicationError(errors.Error):
    """Raised when there is an error in communication module (root class)
    """
    ...


class CommSecretExtractionError(CommunicationError):
    """Raised when there is an error in extracting secrets
    """
    ...


class CommConfigurationError(CommunicationError):
    """Raised when there is an error in opening / parsing a configuration file
    """
    ...


class CommPointError(CommunicationError):
    """Raised when an error occurs related to the concept of points in IOT
    """
    ...

class PlatformType(EnumParent):
    Windows = auto()
    Linux = auto()


class getLocation():
    def __init__(self, /, location: str, *, locationType: str = "file:text/yaml"):
        self.locationType = locationType
        if location is ... or type(location) is not str or location is None:
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
                                raise CommunicationError(
                                    err, errorHandle=errors.ProgrammerErrorHandle(f"YAML error, could not parse the text/yaml at {self.location} with location type {self.locationType}, the file openned though"))
                        case _:
                            raise CommunicationError(
                                f"Unsupported file type: {mimes=}", errorHandle=ProgrammerErrorHandle(f"{self.locationType=} was assumed to be type 'file', but the mime type {mimes} was not recognized"))
                except errors.Error as err:
                    # Propagate error with proper encapsulation of error types
                    raise CommunicationError(err, errorHandle=UserErrorHandle(
                        f"For some reason the file at location {self.location} could not be properly configured with location type {self.locationType}"))
                except FileNotFoundError as err:
                    # Probably not plugged in harddrive
                    raise errors.SimpleUserError(
                        "Secret harddrive probably not plugged in :)", err, f"Wow cool directory", errorHandle=UserErrorHandle(f"The secret harddrive / location set in {PlatformInfo.CONFIG_RELATIVE_LOCATION} could not be found, maybe not plugged in?"))
            case _:
                raise CommunicationError(
                    f"Unsupported location type: {self.locationType=}", errorHandle=ProgrammerErrorHandle("Currently only 'file' is supported as a location type"))

    def __enter__(self):
        return self()

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


class PlatformInfo():
    """Is responsible for platform specific tasks, such as retrieving secrets (absolute locations will differ between platform types) and config files

    requestSecrets(secretHandle: str) -> str
    """

    # Exporting to the config file is counter-intuitive :)
    CONFIG_RELATIVE_LOCATION = "config.yaml"

    def __init__(self, platform: PlatformType = ...) -> None:
        if platform == ...:
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
        def __init__(self, relativeLocation: str) -> None:
            absLocation = os.path.join(
                os.path.dirname(__file__), relativeLocation)
            super().__init__(location=absLocation, locationType="file:text/yaml")

    @property
    def config(self):
        return self._getYAMLConfig(self.CONFIG_RELATIVE_LOCATION)

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


class PointConNetworkType(EnumParent):
    """Represents states of access across networks / internet to projects

    Args:
        EnumParent (PointNetworkType): Type of network access (remote <-> locallyremote <-> remote)
    
    Long Description:
        When you think of an internet of things, their are many different 'angles' or points.
        Consider the local side, my webpage is hosted somewhere and that place is generally referred to as 'local'
        Also consider the locally remote point, I may be right next to my webpage server and so want to access it physically/locally even though it is hosting for other remote places to access it
        Finally, consider the 'largest' side of an IOT (Internet of Things), the remote side. This is where anybody with internet connection can access the IOT and interact with it.

        Every one of these points has their own 'level' of control, and their own ways of communicating with other points.
        So, if (hypothetically of course) we were to create a python class to represent a way of communicating from point to point (Communicator duh).
        And this class would need, probably an Enum, to represent the type of communication wanted by this communicator. If you haven't caught on, this Enum represents just that

        Each Communicator object has only one Point Connection Network Type (probably another class down the track called 'Communication' that manages every possible Point Connection Network Type) which determines how it communicates with other points, over internet, physical Serial, http remote requests, local http requests, etc.
    """
    # Local instance to access locally (same python interpreter) hosted stuff (test webpage, local database, etc)
    LocalToLocal = auto()
    # Local instance to access my remote stuff (basically client)
    LocalToRemote = auto()
    # Remote / Random instance to access my remote stuff (hosted website talking to discordbot)
    RemoteToRemote = auto()
    # Remote instance to control local stuff (wanting to change my desk lights from a holiday)
    RemoteToLocal = auto()


class PointConType(EnumParent):
    Server = auto()
    Node = auto()


class PointCommType():
    """Represents a type of communication between any *TWO* points, over network or serial or other

    Raises:
        CommPointError
    """

    def __init__(self, pointType: PointConType, networkType: PointConNetworkType) -> None:
        self.pointType = pointType
        self.networkType = networkType
        print(
            f"New PointCommType object created for {self.pointType=}, {self.networkType=}")


@final
class Communicator():
    """Is responsible, and the 'API', for communicating from thread/process/project across platforms and the IOT

    requestSecret(secretHandle: str) -> str
      Use to request a secret from the platform-specific secret store, e.g. comm.requestSecret("ryanpinger TOKEN")
    """
    @overload
    def __init__(self, pointCommunicationType: PointCommType):
        ...

    def __init__(self, pointCommunicationType: PointCommType = ..., platformInfo: PlatformInfo = ...) -> None:
        if pointCommunicationType == ...:
            raise errors.InappropriateRequest("No pointCommunicationType specified", errorHandle=ProgrammerErrorHandle(
                "Must provide pointCommunicationType when instinating Communicator"))
        if platformInfo is ...:
            self.platformInfo = PlatformInfo()
        else:
            self.platformInfo = platformInfo

    @staticmethod
    def _getProjects(filePath: str = FILE_PATH) -> dict:
        """Returns a dictionary of projects, with project names as keys and project types as values
        """
        projects = {}
        for dir in os.listdir(filePath):
            if os.path.isdir(os.path.join(filePath, dir)):
                ...
                #
        return projects

    def requestSecret(self, secretHandle: str):
        """Returns the secret associated with the secretHandle
        e.g. comm.requestSecret("ryanpinger TOKEN")
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
    pointInfo = PointCommType()
    comm = Communicator(CommPointError, platformInfo=platformInfo)
    testSecret = comm.requestSecret('ryanpinger TOKEN')
    print(f"{testSecret=}")
