from typing import List
from Smg88 import events  # Testing this :)
from .. testingerrors import catchall, TestError, ExpectedError
from .. import testmanager

tests = testmanager.Tests()


@tests.registertest
@catchall
def test_EventStageConstructorBasic():
    """This is an UNSAFE FUNCTION (wrapped with @catchall) used for testing
    """
    stages: List[events.EventStage] = []
    stages.append(events.EventStage())
    stages.append(events.EventStage("nameHandle positional argument"))

    for stage in stages:
        print(f"Testing {stage=}")
        TestError(hasattr(stage, "nameHandle"))
        TestError(hasattr(stage, "_subscriptions"))
        TestError(hasattr(stage, "_eventBuffer"))
        TestError(hasattr(stage, "eventBuffer"))
        TestError(hasattr(stage, "channels"))
        ExpectedError(hasattr(stage, "stage"))


@tests.registertest
@catchall
def test_EventStageSubscribingBasic():
    stage = events.EventStage()

    trigger = False

    @stage.subscribe
    def testchannel(event: events.Event):
        nonlocal trigger
        TestError(event.channel == "testchannel")
        TestError(event.stage == stage)
        TestError(event.payload == "testdata")
        TestError(event.name == "testname")
        trigger = True

    stage.push(events.Event(
        channel="testchannel", name="testname", payload="testdata"))
    stage.release()

    TestError(trigger)
