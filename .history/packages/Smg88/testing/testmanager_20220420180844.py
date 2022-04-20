"""Used to manage / run / see the results of tests done
"""

from typing import Callable

_registeredTests = []


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