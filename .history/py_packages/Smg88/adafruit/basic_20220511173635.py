from Adafruit_IO import Client
from dotenv import dotenv_values

config = dotenv_values(".env")

username = config["ADAFRUIT_IO_USERNAME"]
key = config["ADAFRUIT_IO_KEY"]

usedGroup = "Smg"


def channelName(num: int = ...) -> int:
    return


workingchannel = "smg88-test.working"


aio = Client(username, key)

aio.send(pingchannel, "ping 123 yay!")
aio.send(pingchannel, "ping discord please :)")
