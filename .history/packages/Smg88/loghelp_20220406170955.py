"""
Should Include:
Buffer classes
"""

import logging


class log():
  def __init__(self, msg, *, level=):
    self.msg = msg


class loggerInterface():
  def __init__(self, logOutput=logging.getLogger(__name__)):
    self.logOutput = logOutput

  def pushLog(log, )
