"""Used to manage / run / see the results of tests done
"""

from typing import Callable, List
import errors
import testing.testingerrors as testingerrors


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

def importTests():
    """Used to import all tests from this module
    """
    import sys
    import os
    import importlib
    import inspect
    importlib.import_module(__name__)
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isfunction(obj):
            if name.startswith("test_"):
                print(f"Importing test {name}")
                importlib.import_module(__name__).registertest(obj)