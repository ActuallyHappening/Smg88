from glob import glob
import os
import sys

from shutil import move
from tempfile import NamedTemporaryFile

__location__ = os.path.dirname(__file__)
print(f"{__location__=} ")


for file in glob(os.path.join(__location__, "*")):
    file = os.path.basename(file)
    if file == "setup.cfg":
        # Open setup.cfg
        print("Found setup.cfg !")
        setupText: str = ""
        _file = os.path.join(__location__, file)
        with open(_file, "r") as setupFile:
            # Read setup.cfg
            setupText = setupFile.read()
            for line in setupFile.split("\n"):
                if line.startswith("version"):
                    # Increment version
                    print("Found version line!")
                    line = line.strip().split("=")
                    version = line[1].strip().split(".")
                    line = f"version = {version[0]}.{version[1]}.{int(version[2]) + 1}\n"
                    # Write setup.cfg
                    setupFile.write(line)
                    setupFile.writelines(setupFile)
        with open(+file, "w") as setupFile:
            setupFile.write(setupText)
