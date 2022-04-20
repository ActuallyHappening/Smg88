from typing import List
import events
from testingerrors import catchall, TestError, ExpectedError
import testmanager


@testmanager.registertest
@catchall
def test_EventConstructor():
    """This is an UNSAFE FUNCTION (wrapped with @catchall) used for testing
    """
    stages: List[events.EventStage] = []
    stages.append(events.EventStage())
    stages.append(events.EventStage("nameHandle positional argument"))

    for stage in stages:
        TestError(hasattr(stage, "nameHandle"))
        TestError(hasattr(stage, "_subscriptions"))
        ExpectedError(hasattr(stage, "stage"))
