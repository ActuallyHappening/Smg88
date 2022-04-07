import Smg88

# These tests are the aims of my package

import logging
from Smg88.loghelp import loggerInterface

rawLogger = logging.getLogger(__name__)

# Returns the same logger object, with a few modifications
rootLogger = loggerInterface(__name__)

rootLogger.addHandler()
