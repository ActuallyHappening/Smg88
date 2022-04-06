"""
Should Include:
Buffer classes
"""

import logging


class loggerInterface():
  def __init__(self, logOutput=logging.getLogger(__name__)):
    self.logOutput = logOutput

  def pushLog()
