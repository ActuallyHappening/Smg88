import json
import os
import shutil
from glob import glob

Download_Folder: str = "C:/Users/verys/Downloads/*"
Destination_Folder: str = "C:/Users/verys/Downloads/TestDestination/"

Tax_Return_Check_String: str = "signal"
Client_Contact_Check_String: str = "Minecraft"

# Get settings from basic cache file json format
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
_config_location = os.path.join(__location__, "settings.json")
try:
  open(_config_location, "x")
except:
  print("First time detected: Creating settings file :)")
with open(_config_location, "w") as config:
  json.loads(config.read())


Ignore_Next_Tax_Return_Check: bool = False
Ignore_Next_Client_Contact_Check: bool = False

Files = glob(Download_Folder)
print(f"Your download files: \n{Files}")
Files.sort(key=os.path.getctime)
Files.reverse()
for file in Files:
  if Tax_Return_Check_String in file and not Ignore_Next_Tax_Return_Check:
    input(
        f"Moving this file: \n  {file}\n to folder \n  {Destination_Folder}\nClose this window to exit")
    shutil.move(file, Destination_Folder)
    Ignore_Next_Tax_Return_Check = True
  if Client_Contact_Check_String in file and not Ignore_Next_Client_Contact_Check:
    input(
        f"Moving this file: \n  {file}\n to folder \n  {Destination_Folder}\nClose this window to exit")
    shutil.move(file, Destination_Folder)
    Ignore_Next_Client_Contact_Check = True
