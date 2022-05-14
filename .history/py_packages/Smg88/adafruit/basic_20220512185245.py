import Adafruit_IO as AIO
from dotenv import dotenv_values

try:
    from .. import errors
except ImportError:
    raise(Exception("I NEED AN ERRORS LIBRARY GIMME!"))


class AIOIntegrationError(errors.Error, AIO.AdafruitIOError):
    # TODO add a parameter to assemble a useful error message when provided an AIO.AdafruitIOError
    ...


config = dotenv_values(".env")

username = config["ADAFRUIT_IO_USERNAME"]
key = config["ADAFRUIT_IO_KEY"]

usedGroup = "smg88-io-dot-adafruit-dot-com-qad4-group-v1"

workingchannel = f"{usedGroup}.testing123"


aio = AIO.Client(username, key)


def post(data: AIO.Data = AIO.Data(warning="<DEFAULT DATA PASSED TO postTO>"), /, name: o_str = ..., *, group: o_str = usedGroup, feed: o_str = workingchannel,) -> AIO.Data:
    """Posts data to the given feed and handles edge cases"""

    @errors.runAndRaise(AIO.AdafruitIOError, AIOIntegrationError("Adafruit IO Error"))
    def _(): aio.create_data(feed, data)


aio.send(pingchannel, "ping 123 yay!")
aio.send(pingchannel, "ping discord please :)")
