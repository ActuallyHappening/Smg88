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
                VERSION = json.loads(libraryJSONFile.read())["version"].strip()
                _version = VERSION.split('.')
                new = f"{_version[0]}.{_version[1]}.{int(_version[2]) + 1}"  # e.g. v0.1.0 --> v0.1.1
                _newLibraryFile = _newLibraryFile.replace(VERSION, new)
            with open(libraryFile, "w") as libraryJSONFile:
                libraryJSONFile.write(_newLibraryFile)
            return VERSION


def main():
    incrementconfig()


if __name__ == "__main__":
    main()
