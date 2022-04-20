"""Defines a bunch of errors that can be raised by testing functions used in the testing package/folder

Raises:
    errors.InappropriateRequest: When function calls are used incorrectly (DON'T HANDLE)
    WrapperError: When using the decorator @catchall, will raise instead of errors propagated from the function being tested

"""

import functools
from typing import Callable
from Smg88 import errors


class TestingError(errors.Error):
    ...


class TestingErrorHandle(errors.ErrorHandle):
    handleName = "Testing Error Handle: "


class WrapperError(TestingError):
    ...


class WrapperErrorHandle(errors.ErrorHandle):
    handleName = "Wrapper Error Handle: "


def catchall(func: Callable = ...):
    """Used to decorate functions that are being tested, will catch and appropriately handle any errors raised in calling function

    Args:
        func (Callable): Will call this function (decorator) and properly propagate errors

    Raises:
        WrapperError: Raised instead of any other error (conforms propagated errors to WrapperError)

    Returns:
        Decorated function
    """
    if func is ...:
        raise errors.InappropriateRequest("Must provide a function to decorate", errorHandle=TestingErrorHandle(
            "Properly use catchall function as a decorator (pls)"))

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as err:
            raise WrapperError(err, errorHandle=WrapperErrorHandle(
                "While testing, an error ocurred in a wrapped function"))
    return wrapper


class ConditionalError(TestingError):
    def __init__(self, condition: bool, /, *, check: bool = True):
        super().__init__(f"ConditionalError: {condition!r}")
        if bool(condition) is bool(check):
            raise self


class ExpectedError(ConditionalError):
    def __init__(self, condition: bool):
        super().__init__(condition=condition, check=False)


class TestError(ConditionalError):
    def __init__(self, condition: bool):
        super().__init__(condition=condition, check=True)
