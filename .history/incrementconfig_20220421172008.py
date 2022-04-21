from glob import glob
import os
import sys

__location__ = os.path.dirname(__file__)
print(f"{__location__=} ")


for file in glob(__location__):
    if file == "setup.cfg":
        # Open setup.cfg
        with open(os.path.join(__location__, file), "r+") as f:
            # Read setup.cfg
            setup_cfg = f.read()
            print(f"{file=}:\n{setup_cfg=}")
