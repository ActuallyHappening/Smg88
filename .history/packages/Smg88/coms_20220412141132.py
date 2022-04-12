from enum import auto
from loghelp import EnumParent


class PointRole(EnumParent):
    Server = auto()
    Node = auto()


class PointType(EnumParent):
    LocalToLocal = auto()
    LocalToRemote = auto()
    RemoteToLocal = auto()
    RemoteToRemote = auto()


class Communicator():
    """Represents a communication 'stream' or option for communicating with something, usually a Point

    isasync: bool = True
    requestRolt(): PointRole
    requestType(): PointType

    _send(): str
        Send a 'packet' or item of data
    _buffer: str
        An array that represents the data received
    _get() : str
        Takes an item off the _buffer and gives it to the caller
    """
    isasync: bool

    _buffer: List[str]

    def __init__(self, isasync: bool = True):
        self.isasync = isasync
        self._buffer = []


class UserCommunicator(Communicator):
    ...


class Communication():
    """Represents a possible communication 'target' and provides an array of Communicator objects to use to communicate with is

    communicators: List[Communicator]
    requestRole(): PointRole
    requestType(): PointType
    """

    def __init__(self) -> None:
        ...

class Point():
    """Class that represents a single point (to current python interpreter) in the IOT

    role: PointRole
    type: PointType

    requestPoints(): Dict
        Returns a dictionary of Communication objects for each point found that responded in my IOT
    requestServers(): Dict
        Returns a dictionary of Communication obejcts for each server found that responded in my IOT
    requestNodes(): Dict
        Returns a dictionary of Communication objects for each node found that responded in my IOT
    
    """

    def __init__(self):
        ...


def tests():
    """Tests for the coms.py module"""
    p = Point()
    ...

if __name__ == "__main__":
    tests()
