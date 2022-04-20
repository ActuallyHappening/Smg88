"""Used to manage / run / see the results of tests done
"""

from typing import Callable

_registeredTests = []


class Test():
    func: Callable
    name: str

    def __init__(self, /, func: Callable = ..., *, name: str = ...):
        self.func = func
        if self.func is ...:
            raise errors.InappropriateRequest("Must provide a function to test", errorHandle=TestingErrorHandle(
                "Properly use test function as a decorator (pls)"))
        self.name = name


def registertest(func: Callable) -> Callable:
    """Used to register a function as a test
    """
    _registeredTests.append(func)
    return func


def runtests():
    """Used to run all registered tests
    """
    for test in _registeredTests:
        test()
