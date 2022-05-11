import Adafruit_IO as AIO
from dotenv import dotenv_values

config = dotenv_values(".env")

username = config["ADAFRUIT_IO_USERNAME"]
key = config["ADAFRUIT_IO_KEY"]

usedGroup = "smg88-io-dot-adafruit-dot-com-qad4-group-v1"

workingchannel = f"{usedGroup}.testing123"


aio = AIO.Client(username, key)


def post(data: AIO.Data = AIO.Data(warning="<DEFAULT DATA PASSED TO postTO>"), feed: str = workingchannel,) -> int:
    aio.create_data(feed, data)


aio.send(pingchannel, "ping 123 yay!")
aio.send(pingchannel, "ping discord please :)")
