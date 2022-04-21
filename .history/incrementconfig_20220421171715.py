import os
import sys

__location__ = os.path.abspath(__file__)

from glob import glob

for file in glob(__location__):
    if file == "setup.cfg":
        # Open setup.cfg
        with open(os.path.join(__location__, file), "r") as f:
            # Read setup.cfg
            setup_cfg = f.read()
