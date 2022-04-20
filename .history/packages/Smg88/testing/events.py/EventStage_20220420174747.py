from typing import List
import events

from testingerrors import TestingError, ExpectedError


def test_EventConstructor():
    stages: List[events.EventStage] = []
    stages.append(events.EventStage())
    _stage = events.EventStage("nameHandle positional argument")

    for stage in stages:
        TestingError(hasattr(stage, "nameHandle"))
