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
        with open(os.path.join(__location__, file), "r+") as setupFile:
            # Read setup.cfg
            for line in setupFile:
                if line.startswith("version"):
                    # Increment version
                    print("Found version !")
                    line = line.strip().split("=")
                    version = line[1].strip().split(".")
                    line = "=".join(line)
                    # Write setup.cfg
                    setupFile.seek(0)
                    setupFile.write(line)
                    setupFile.truncate()
                    break
