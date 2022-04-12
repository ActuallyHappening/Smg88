from enum import auto
from typing import List, overload
from Smg88.errors import ProgrammerErrorHandle
from loghelp import EnumParent
import errors
from errors import Error


class PointRole(EnumParent):
    Server = auto()
    Node = auto()


class PointType(EnumParent):
    LocalToLocal = auto()
    LocalToRemote = auto()
    RemoteToLocal = auto()
    RemoteToRemote = auto()


class PacketItem():
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
    _bufferSend: List[Item]
        An array that represents data yet to be sent (on next eventloop perhaps?)

    _send(num: int): Item
        Asynchronously sends (num number of) items from the _bufferSend start
    _receive(*packets): Item
        Is called to receive packet/s, appends then to _buffer end

    """
    isasync: bool

    _buffer: List[str]
    _bufferSend: List[PacketItem]

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

    def send(self, *packets: PacketItem):
        raise NotImplementedError

    def _receive(self, *packets: PacketItem):
        raise NotImplementedError

    def _send(self, *packets: PacketItem):
        raise NotImplementedError


class CommunicatorErrors(errors.Errors):
    """Errors for the Communicator class"""
    ...


class CommunicatorBufferError(CommunicatorErrors):
    """Errors for the Communicator class related to buffers"""
    ...


class CommunicatorEmptyBuffer(CommunicatorBufferError):
    """Raised when strict and the buffer is empty"""
    ...


class CommunicatorPurgeBuffer(CommunicatorBufferError):
    """Raised when strict and the buffer is purged"""
    ...

class UserCommunicator(Communicator):
    def send(self, *packets: PacketItem) -> None:
        (self._bufferSend.append(packet) for packet in packets)

    @overload
    def get(self, num: int = 1) -> List[PacketItem]:
        ...

    @overload
    def get(self, all: bool = True) -> List[PacketItem]:
        ...

    def get(self, /, num: int = 1, *, all: bool = False, retain: bool = ..., strict: bool = True) -> List[PacketItem]:
        if all:
            num = len(self._buffer)
            if not retain:
                # TODO Add warning for purging self._buffer when !strict
                if strict:
                    raise CommunicatorPurgeBuffer(errorHandle=ProgrammerErrorHandle(
                        "Try not to set all=True and retain=False else you will purge (delete the whole of) the self._buffer!"))
        if num > len(self._buffer):
            raise CommunicatorEmptyBuffer(errorHandle=ProgrammerErrorHandle(
                "Do not request more items than are in the buffer, use all=True and/or retain=True"))
        if retain:

        else:
        return [self._buffer.pop(0) for i in range(num)]

    def _receive(self, *packets: PacketItem) -> None:
        self._bufffer.append(PacketItem(input("User Communicator: ")))

    def _send(self, num: int = 1) -> None:
        print(f"P{i}: {self._buffer.pop(0)}\n" for i in range(num))


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
        Returns a dictionary of Communication objects for each server found that responded in my IOT
    requestNodes(): Dict
        Returns a dictionary of Communication objects for each node found that responded in my IOT

    """

    def __init__(self):
        ...


def tests():
    """Tests for the coms.py module"""
    p = Point()
    test = UserCommunicator()
    test.send(PacketItem("Hello world!"))
    test.send(test.get())
    ...


if __name__ == "__main__":
    tests()
