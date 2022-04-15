from typing import Callable, Dict


class EventStage():
  """Represents a place for events to occur
  Events can be posted to this stage by instancing the 'Event' object, which is suggested to be done through a class method attached to the stage that is wanting to be posted to
  All events have a 'channel' and 'name' property, and such an 'EventFilter' object must be passed to subscribe to events on a stage, which is simply a function that takes an event and returns a boolean representing whether the event should be passed to the subscriber

  _subscriptions
  """
  _subscriptions: Dict[Callable, Callable]
  def __init__(self, /, nameHandle: str = "CLI"):
    ...
