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
        TestError(hasattr(stage, "_eventBuffer"))
        TestError(hasattr(stage, "eventBuffer"))
        TestError(hasattr(stage, "channels"))
        ExpectedError(hasattr(stage, "stage"))


@testmanager.registertest
@catchall
def test_EventSubscribing():
    stage = events.EventStage()

    trigger = False

    @stage.subscribe
    def testchannel(event: events.Event):
        TestError(event.channel == "testchannel")
        TestError(event.stage == stage)
        TestError(event.data == "testdata")
        trigger = True
