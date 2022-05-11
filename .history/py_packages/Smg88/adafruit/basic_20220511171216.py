from Adafruit_IO import Client
from dotenv import dotenv_values

config = dotenv_values(".env")

username = config["ADAFRUIT_IO_USERNAME"]
key = config["ADAFRUIT_IO_KEY"]

pingchannel = "smg88-test.ping"
debugchannel = "smg88-test.debug"
warningchannel = "smg88-test.warning"
errorchannel = "smg88-test.error"

workingchannel = "smg88-test.working"


aio = Client(username, key)

aio.send(pingchannel, "ping 123 yay!")
aio.send(pingchannel, "ping discord please :)")
