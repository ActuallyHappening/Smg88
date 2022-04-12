"""
Should Include:
Basic error classes and their descriptors
"""

# Repeated code with __init__ and extra, will eventually be removed or multiple inheritance from CustomError but that


class UserErrorHandle():
  """Class that handles errors the user can identify / recover from
  """

  def __init__(self, msg, *msgs, **extra):
    self.msg = f"Message: {msg}" + "\n" + '\n'.join(msgs)
    self.extras = extra

  def __str__(self):
    return f"{self.msg}" + "\n" + "\n".join(f"{k}: {v}" for k, v in self.extras.items())


class Error(Exception):
  """Exception class that is root of all custom exceptions
  """

  def __init__(self, msg, *msgs, userErrorHandle: UserErrorHandle = ..., **extra):
    msg = str(msg)
    _msgs = [str(m) for m in msgs]
    _msgs = '\n'.join(_msgs)
    self.msg = f"Message: \n{msg}\n{_msgs}"
    self.extras = extra
    self.userErrorHandle = userErrorHandle

  def __str__(self):
    return f"{self.msg}\n" + "\n".join(f"{k}: {v}" for k, v in self.extras.items()) + "\n" + str(self.userErrorHandle)


class ProgrammerError(Error):
  """Exception class that is root of all internal / implementation / programmer related errors
  """
  ...


class InappropriateRequest(ProgrammerError):
  """Exception class that is raised when a request on some programming object / function / property is inappropriate
  """
  ...
