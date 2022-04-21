from glob import glob
import os
import sys
import subprocess


__location__ = os.path.dirname(__file__)
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


def uploadtwine():
    subprocess.run(["py", "-m", "twine", "upload", "-r", "pypi",
                   "--verbose", "--non-interactive", "--skip-existing", "-u", "Smartguy87", "-p", "Smg!88'{^[(", "dist/*"])


def main(action: str):
    if action == "incrementsetup":
        print("Incrementing config ...")
        incrementconfig()
    elif action == "uploadtwine":
        print("Uploading twine ...")
        uploadtwine()
    elif action == "successful":
        print(
            "You macro finished successfully :)\nLETS GOOOO YIPEE HAVE JOY IT IS FINISHED!!")
    elif action == "finished":
        print(
            "You macro finished :)\nMaybe it worked, just check to see :)")
    elif action == "gitautocommit":
        print("Auto Commiting to git ...")
        subprocess.run(["git", "add", "-A"])
        subprocess.run(["git", "commit", "-a", "-m", "Autocommityay"])
    else:
        print(f"MACRO FAILED oh no! {action=} was not matched :(")


if __name__ == "__main__":
    main(sys.argv[1])
