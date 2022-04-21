from typing import List
from .. .. import events
from .. testingerrors import catchallf, TestError, ExpectedError
from .. import testmanager

tests = testmanager.Tests()


@tests.registertest
@catchallf
def test_EventConstructorBasic():
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


@tests.registertest
@catchallf
def test_EventSubscribingBasic():
    stage = events.EventStage()

    trigger = False

    @stage.subscribe
    def testchannel(event: events.Event):
        TestError(event.channel == "testchannel")
        TestError(event.stage == stage)
        TestError(event.payload == "testdata")
        TestError(event.name == "testname")
        trigger = True

    stage.push(events.Event(
        channel="testchannel", name="testname", payload="testdata"))
    stage.release()

    TestError(trigger)