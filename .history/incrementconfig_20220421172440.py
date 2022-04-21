from glob import glob
import os
import sys

__location__ = os.path.dirname(__file__)
print(f"{__location__=} ")


for file in glob(os.path.join(__location__, "*")):
    file = os.path.basename(file)
    if file == "setup.cfg":
        # Open setup.cfg
        print("Found setup.cfg !")
        with open(os.path.join(__location__, file), "r+") as f:
            # Read setup.cfg
            setup_cfg = f.read()