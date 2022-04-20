import errors

class TestingError(errors.Error):
  ...

class WrapperError(TestingError):
  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)

class WrapperErrorHandle(errors.ErrorHandle):
  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)

def catchall(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except BaseException as err:
      raise WrapperError(err)
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
