from enum import Enum
from glob import glob
import os
import sys

__location__ = os.path.dirname(__file__)
print(f"{__location__=} ")


class ActionType(Enum):
    """
    Enum for actions
    """
    incrementconfig = 1
    uploadtwine = 2


def incrementconfig():
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
                for line in setupText.split("\n"):
                    if line.startswith("version"):
                        # Increment version
                        print("Found version line!")
                        previous = line
                        version = line.strip().split("=")[1].strip().split(".")
                        new = f"version = {version[0]}.{version[1]}.{int(version[2]) + 1}"
                        # Update whole text with new version
                        setupText = setupText.replace(previous, new)
            with open(_file, "w") as _setupFile:
                _setupFile.write(setupText)


def uploadtwine():
    ...


def main(action: str):
    if action == ActionType.incrementconfig.name:
        print("Incrementing config ...")
        incrementconfig()
    elif action == ActionType.uploadtwine.name:
        print("Uploading twine ...")
        uploadtwine()


if __name__ == "__main__":
    main(sys.argv[1])
