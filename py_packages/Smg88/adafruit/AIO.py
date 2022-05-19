import Adafruit_IO as AIO
from dotenv import dotenv_values

try:
    #from .. import errors
    #from ..typehelp import o_str
    69
except ImportError:
    raise(Exception("I NEED AN ERRORS LIBRARY GIMME!"))


''' class AIOIntegrationError(errors.Error, AIO.AdafruitIOError):
    # TODO add a parameter to assemble a useful error message when provided an AIO.AdafruitIOError
    ... '''


config = dotenv_values(".env")

username = config["ADAFRUIT_IO_USERNAME"]
key = config["ADAFRUIT_IO_KEY"]


aio = AIO.Client(username, key)

aio.send("oppo.oppo-out-react-oppo-notification", "__test__ 2")


def post(data: str | AIO.Data, feed: str) -> AIO.Data:
    """Posts data to the given feed and handles edge cases"""
    data = aio.send(feed, data)

    ''' @errors.runAndRaise(AIO.AdafruitIOError, AIOIntegrationError("Adafruit IO Error"))
    def _(): data = aio.send(feed, data) '''

    return data


#aio.send(pingchannel, "ping 123 yay!")
#aio.send(pingchannel, "ping discord please :)")
