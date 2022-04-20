"""Used to manage / run / see the results of tests done
"""

from typing import Callable, List
import errors
import testing.testingerrors as testingerrors


class Test():
    func: Callable
    name: str

    def __init__(self, /, func: Callable = ..., *, name: str = ...):
        self.func = func
        if self.func is ...:
            raise errors.InappropriateRequest("Must provide a function to test", errorHandle=testingerrors.TestingErrorHandle(
                "Properly use test function as a decorator (pls)"))
        self.name = name
        if self.name is ...:
            self.name = self.func.__name__

    def run(self):
        self.func()


_registeredTests: List[Test] = []


def registertest(func: Callable) -> Callable:
    """Used to register a function as a test

    You can use this as a decorator, reminder :)
    """
    _registeredTests.append(Test(func))
    return func


def runtests():
    """Used to run all registered tests
    """
    for test in _registeredTests:
        test.run()
