import Adafruit_IO
from dotenv import dotenv_values

config = dotenv_values(".env")

username = config["ADAFRUIT_IO_USERNAME"]
key = config["ADAFRUIT_IO_KEY"]

usedGroup = "Smg88 io.adafruit.com QAD4 Group v1"

workingchannel = "smg88-test.working"


aio = Client(username, key)


def postTo(feed: str = usedGroup, data: Adafruit_IO.Data) -> int:
    return


aio.send(pingchannel, "ping 123 yay!")
aio.send(pingchannel, "ping discord please :)")
