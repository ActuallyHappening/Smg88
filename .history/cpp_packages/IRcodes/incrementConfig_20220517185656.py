
from glob import glob
import json
import os

__location__ = os.path.dirname(__file__)


print(f"{__location__=} ")


def getAndUpdateConfigFile():
    for file in glob(os.path.join(__location__, "*")):
        file = os.path.basename(file)
        if file == "library.json":
            # Open library.json
            print("Found library.json found !")
            libraryFile = os.path.join(__location__, file)
            _newLibraryFile = ""
            VERSION = "__UNKNOWN__"
            oldVersion = "__UNKNOWN__"
            with open(libraryFile, "r") as libraryJSONFile:
                _newLibraryFile = libraryJSONFile.read()
                # print(f"{_newLibraryFile=}")
                VERSION = json.loads(_newLibraryFile)["version"].strip()
                oldVersion = VERSION[1:]  # remove the first 'v'
                _version = VERSION.split('.')
                newVersion = f"{_version[0]}.{_version[1]}.{int(_version[2]) + 1}"  # e.g. v0.1.0 --> v0.1.1
                _newLibraryFile = _newLibraryFile.replace(VERSION, newVersion)
                VERSION = newVersion[1:]  # remove the first 'v'
            with open(libraryFile, "w") as libraryJSONFile:
                libraryJSONFile.write(_newLibraryFile)


def scanSRCandUpdateVersion(oldVersion, newVersion):
    print("Scanning src folder for version updates ...")
    for file in glob(os.path.join(__location__, "src/*")):
        updateFile(file, oldVersion, newVersion)
    for file in glob(__location__):
        if file == ""


def updateFile(file, oldVersion, newVersion):
    fileName = os.path.basename(file)
    fileText = "__default__"
    with open(file, "r") as _file:
        # print(f"{fileName=}")
        fileText = _file.read()
        _fileText = ""
        if "SCAN VERSION" not in fileText:
            return
        for line in fileText.split("\n"):
            if "SCAN VERSION" in line:
                print(f"Replacing {oldVersion} with {newVersion} in {fileName}")
                if oldVersion not in line:
                    print("   Old version not found in file even though // SCAN VERSION was found !")
                line = line.replace(oldVersion, newVersion)  # .replace("// SCAN VERSION", f"// SCAnN VERSION {oldVersion} --> {newVersion}")
                print(f"  New Line: {line=}")
            _fileText += line + "\n"
        fileText = _fileText
    with open(file, "w") as _file:
        _file.write(fileText)


def main():
    oldVersion, newVersion = getAndUpdateConfigFile()
    scanSRCandUpdateVersion(oldVersion, newVersion)


if __name__ == "__main__":
    main()
