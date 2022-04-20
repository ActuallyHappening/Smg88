"""Used to manage / run / see the results of tests done
"""

from typing import Callable, List
from Smg88 import errors
import testing.testingerrors as testingerrors
import os
import sys
import inspect
import importlib
import re

__location__ = os.path.dirname(__file__)


class Test():
    func: Callable
    name: str

    def __init__(self, func: Callable = ..., *, name: str = ...):
        self.func = func
        if self.func is ...:
            raise errors.InappropriateRequest("Must provide a function to test", errorHandle=testingerrors.TestingErrorHandle(
                "Properly use Test constructor"))
        self.name = name
        if self.name is ...:
            self.name = self.func.__name__

    def run(self):
        self.func()
        print(f"Test {self.name} passed")


class Tests():
    _registeredTests: List[Test] = []

    def registertest(self, func: Callable) -> Callable:
        """Used to register a function as a test

        You can use this as a decorator, reminder :)
        """
        self._registeredTests.append(Test(func))
        return func

    def runtests(self):
        """Used to run all registered tests
        """
        print("Running tests ....")
        for test in self._registeredTests:
            test.run()


allTests: List[Tests] = []


def importTests():
    """Used to import all tests from within this module's surrounding folders
    """
    for file in os.listdir(__location__):
        if file[:2] != "__":
            if file[-3:] == ".py":
                _file = os.path.join(__location__, file)
                #print(f"Importing tests {_file=} from {__location__}")
                # importlib.import_module(_file)
                for name, obj in inspect.getmembers(
                        sys.modules[_file]):
                    print(f"Cool! {name=}, {obj=}")
                    if inspect.isfunction(obj):
                        if name.startswith("test_"):
                            print(f"Importing test {name}")
                            allTests.append(
                                importlib.import_module(_file).tests)
