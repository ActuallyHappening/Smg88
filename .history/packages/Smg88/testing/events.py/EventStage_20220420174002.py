from typing import List
import events


def test_EventConstructor():
    _stageEmpty = events.EventStage()
    _stage = events.EventStage("nameHandle positional argument")

    stages: List[events.EventStage] = [_stageEmpty, _stage]

    for stage in stages:
        assert hasattr(stage, "nameHandle")
