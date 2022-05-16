__location__ = os.path.dirname(__file__)
from glob import glob


print(f"{__location__=} ")


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


def main():
    incrementconfig()


if __name__ == "__main__":
    main()
