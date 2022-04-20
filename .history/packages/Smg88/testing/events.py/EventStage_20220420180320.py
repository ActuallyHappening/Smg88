from typing import List
import events
from testingerrors import catchall

from testingerrors import TestingError, ExpectedError


def test_EventConstructor():
    stages: List[events.EventStage] = []

    stages.append(events.EventStage())
    stages.append(events.EventStage("nameHandle positional argument"))

    for stage in stages:
        TestingError(hasattr(stage, "nameHandle"))
