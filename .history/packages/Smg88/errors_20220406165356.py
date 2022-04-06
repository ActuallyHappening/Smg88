"""Should Include:
Basic error classes and their descriptors
"""


class CustomError(Exception):
  ...


class ProgrammerError(CustomError):
  """
  Exception class that is root of all programmer related exceptions
  """
  ...


class InappropriateRequest(ProgrammerError):
  """
  Exception class that is raised when a request on some programming object / function / property is inappropriate
  """
  ...
