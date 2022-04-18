from typing import Callable, Dict, List
import errors


class Event():
  channel: str
  name: str

  def __init__(self, channel: str, name: str) -> None:
    self.channel = channel
    self.name = name


def EventFilter(channelsAccepted: List[str] = ..., namesAccepted: List[str] = ...):
  def _filter(event: Event) -> bool:
    if namesAccepted is not None:
      if event.name not in namesAccepted:
        return False
    if channelsAccepted is not None:
      if event.channel not in channelsAccepted:
        return False
    return True
  return _filter

class EventStage():
  """Represents a place for events to occur
  Events are objects that have a channel and a name, all events are passed to all subscribers of that event's channel

  Events can be posted to this stage by instancing the 'Event' object, which is suggested to be done through a class method attached to the stage that is wanting to be posted to, and then calling the 'post' method on the stage
  All events have a 'channel' and 'name' property, to subscribe 

  nameHandle: str
    A common name for the EventStage, needed to connect to the EventStage
  subscriptions: Dict  [str, Callable.__name__]
    Is a property exposing the subscriptions of the stage, the key is the channel and the value is the name of the subscriber's function


  _subscriptions: Dict  [str, Callable]
    A dictionary of channel names to functions that are subscribed to that channel name
  _eventBuffer: List[Event]
    A buffer of events to post to the stage
  """
  _subscriptions: Dict[str, Callable] = ...
  nameHandle: str = ...

  _eventBuffer: List[Event] = ...

  def __init__(self, nameHandle: str = ...) -> None:
    self.nameHandle = nameHandle
    if self.nameHandle is ...:
      # TODO add warning for instinating an EventStage without a nameHandle
      ...
    self._subscriptions = {}

  def post(self, event: Event = ..., /, **kwargs) -> None:
    if event is ...:
      # TODO add warning for not passing an event
      raise errors.InappropriateRequest("No event was passed to the post method",
                                        errorHandle=errors.ProgrammerErrorHandle("Must pass an event to the post method"))
    self._eventBuffer.append(event)

  def _post(self, /, num: int = 1, *, all: bool = False, retain: bool = ..., **kwargs) -> None:
    if all:
      if retain is ...:
        retain = True
      if not retain:
        # TODO Warn for purging buffer
        ...
      self._postn(num=len(self._eventBuffer), retain=bool(retain) ** kwargs)

  def _postn(self, /, num: int = 1, *, retain: bool = False, **kwargs) -> None:
    for n in range(num):
      self._eventBuffer.pop(0)

  def _handle(self, event: Event) -> None:
    if event.channel in self._subscriptions.keys():
      self._subscriptions[event.channel](event=event)
