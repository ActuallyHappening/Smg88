from enum import auto
from typing import List
from loghelp import EnumParent


class PointRole(EnumParent):
    Server = auto()
    Node = auto()


class PointType(EnumParent):
    LocalToLocal = auto()
    LocalToRemote = auto()
    RemoteToLocal = auto()
    RemoteToRemote = auto()


class Item():
    _content: List[str]

    def __init__(self, *strings):
        self._content = strings

    @property
    def content(self):
        return self._content

    @property
    def msg(self):
        return self._content[0]

    def __str__(self) -> str:
        return self.msg


class Communicator():
    """Represents a communication 'stream' or option for communicating with something, usually a Point

    isasync: bool = True
    requestRole(): PointRole
    requestType(): PointType
    buffer: List[Item] property get
    bufferSend: List[Item] property get

    get(num: int): Item
        Takes (num number of) items off the _buffer and gives it to the caller
    send(*items: Item): Item
        Takes items and puts it on the _bufferSend

    _buffer: List[Item]
        An array that represents the data received  
    _buffersend: List[Item]
        An array that represents data yet to be sent (on next eventloop perhaps?)
    
    _send(num: int): Item
        Asynchronously sends (num number of) items from the _bufferSend
    _receive(*packets): Item
        Is called to receive packet/s
     
    """
    isasync: bool

    _buffer: List[str]
    _bufferSend: List[Item]

    def __init__(self, isasync: bool = True):
        self.isasync = isasync
        self._buffer = []
        self._bufferSend = []

    @property
    def buffer(self):
        return self._buffer

    @property
    def bufferSend(self):
        return self._bufferSend

    def get(self, num: int):
        raise NotImplementedError

    def send(self, *packets: Item):
        raise NotImplementedError

    def _receive(self, *packets: Item):
        raise NotImplementedError

    def _send(self, *packets: Item):
        raise NotImplementedError


class UserCommunicator(Communicator):
    def send(self, *packets: Item):
        print(*packets)

    def get(self, *packets: Item):
        return Item(input("User Communicator: "))


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
    test = UserCommunicator()
    test.send(Item("Hello world!"))
    test.send(test.get())
    ...

if __name__ == "__main__":
    tests()
