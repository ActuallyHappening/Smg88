"""Enables my python scripts to communicate between running instances and to read secrets from pre-set physical files
"""


class CommError(Exception):
  """Raised when there is an error in communication
  """
  pass


class SecretExtractionError(CommError):
  """Raised when there is an error in extracting secrets
  """
  pass


class Communicator():
  def requestSecret(secretHandle: str):
    """Returns the secret associated with the secretHandle
    """
    match secretHandle:
      case "ryanpinger TOKEN":
        return "to be inserted"
