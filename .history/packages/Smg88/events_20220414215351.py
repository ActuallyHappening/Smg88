from typing import Callable, Dict, List


class Event():
  channel: str
  name: str

  def __init__(self, channel: str, name: str) -> None:
    self.channel = channel
    self.name = name


def EventFilter(channelsAccepted: List[str], namesAccepted: List[str] = ...):
  def _filter(event: Event) -> bool:
    if namesAccepted is not None:
      if event['name'] not in namesAccepted:
        return False
    if channelsAccepted is not None:
      if event['channel'] not in channelsAccepted:
        return False
    return True

class EventStage():
  """Represents a place for events to occur
  Events can be posted to this stage by instancing the 'Event' object, which is suggested to be done through a class method attached to the stage that is wanting to be posted to
  All events have a 'channel' and 'name' property, and such an 'EventFilter' function must be passed to subscribe to events on a stage, which is simply a function that takes an event and returns a boolean representing whether the event should be passed to the subscriber

  _subscriptions: Dict  [Callable, Callable]
  """
  _subscriptions: Dict[Callable, Callable]

  def __init__(self, nameHandle: str = "CLI"):
    ...
