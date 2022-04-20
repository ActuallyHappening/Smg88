from typing import List
import events
from testingerrors import catchall

from testingerrors import TestingError, ExpectedError


@catchall
def test_EventConstructor():
    """This is an UNSAFE FUNCTION (wrapped with @catchall) used for testing
    """
    stages: List[events.EventStage] = []
    stages.append(events.EventStage())
    stages.append(events.EventStage("nameHandle positional argument"))

    for stage in stages:
        TestingError(hasattr(stage, "nameHandle"))
