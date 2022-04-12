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
