__location__ = os.path.dirname(__file__)
from glob import glob
import json
import os


print(f"{__location__=} ")


def incrementconfig():
    for file in glob(os.path.join(__location__, "*")):
        file = os.path.basename(file)
        if file == "library.json":
            # Open library.json
            print("Found library.json found !")
            libraryFile = os.path.join(__location__, file)
            _newLibraryFile = ""
            VERSION = "__UNKNOWN__"
            with open(libraryFile, "r") as libraryJSONFile:
                _newLibraryFile = libraryJSONFile.read()
                VERSION = json.loads(libraryJSONFile.read())["version"].strip().split(".")
                new = f"{VERSION[0]}.{VERSION[1]}.{int(VERSION[2]) + 1}"  # e.g. v0.1.0 --> v0.1.1
                _newLIBRARYJSON = _newLibraryFile.replace(VERSION, new)
            with open(libraryFile, "w") as libraryJSONFile:
                libraryJSONFile.write(_newLibraryFile)
            return VERSION
            with open(libraryFile, "r") as setupFile:
                # Read setup.cfg
                setupText = setupFile.read()
                for line in setupText.split("\n"):
                    if line.startswith("version"):
                        # Increment version
                        print("Found version line!")
                        previous = line
                        VERSION = line.strip().split("=")[1].strip().split(".")
                        new = f"version = {VERSION[0]}.{VERSION[1]}.{int(VERSION[2]) + 1}"
                        # Update whole text with new version
                        setupText = setupText.replace(previous, new)
            with open(libraryFile, "w") as _setupFile:
                _setupFile.write(setupText)


def main():
    incrementconfig()


if __name__ == "__main__":
    main()
