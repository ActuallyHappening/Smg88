import functools
from json import JSONDecodeError
import json
from typing import Callable, Dict, List
import loghelp
from errors import ProgrammerError, ProgrammerErrorHandle, SafeCatchAll
import errors


class EventError(errors.Error):
    """The base class for all errors in this module
    """
    ...


class EventSubscriberCallbackError:
    """Class of error parenting all errors related to subscriber callbacks
    """
    ...


class EventSubscriberCallbackErrorNotCallable(EventSubscriberCallbackError):
    """Error raised when a subscriber callback is not callable
    """
    ...


class Event():
    """Event class represents an event that can be posted and subscribed to

    Attributes:
      channel: str
        The channel to which the event is said to be existing in
      name: str
        The name of the event, used for easy identification
      payload: str
        The payload of the event, used to convey the information of the event, usually in JSON format
    """
    channel: str = ...
    name: str = ...

    payload: str = ...

    def __init__(self, *, channel: str = ..., name: str = ..., payload: str = ..., **kwargs) -> None:
        self.channel = channel
        if self.channel is ...:
            # TODO add warning for instinating event without channel handle
            ...
        if type(self.channel) is not str:
            # TODO add warning for instinating event with non-serializable (not str) channel handle
            ...
        self.name = name
        if self.name is ...:
            # TODO add warning for instinating event without name handle
            ...
        if type(self.name) is not str:
            # TODO add warning for instinating event with non-serializable (not str) name handle
            ...
        self.payload = payload
        if self.payload is ...:
            # TODO add warning for instinating event without payload
            ...
        if type(self.payload) is not str:
            # TODO add warning for instinating event with non-serializable (not str) payload
            ...

    def send(self, /, stage=..., **kwargs) -> None:
        """Posts the event to the given EventStage as if EventStage.post(event=self) was called (hint it is : )

          Args:       
            stage: EventStage
              The stage to which the event is sent too
              Note: Annotation for stage is not possible as this is a convenience method
        """
        try:
            stage.post(event=self)
        except SafeCatchAll as err:
            # TODO add warning for eventstage post failure
            raise err


class HeartBeatEvent(Event):
    """Event class representing a heartbeat event

    For __docs__ on Event, see Event.__doc__ NOT here!
    Attributes:
      channel: str = "Smg88::HeartBeat"
        The channel to which the event is said to be existing in
      name: str = f"Smg88 HeartBeat ({self.count}) at about {loghelp.now()}"
      payload: str = JSON Format below:
        {
          "count": int,
          "approxtime": str,
        }
    """
    count: int = ...

    def __init__(self, count: int = -1, *, channel: str = ..., name: str = ..., timestr: str = ..., payload: str = ..., **kwargs) -> None:
        self.count = count
        if type(self.count) is not int:
            # TODO add warning for non-serializable (not int) count
            ...
        self.timestr = timestr
        if self.timestr is ...:
            self.timestr = loghelp.now()
        if type(self.timestr) is not str:
            # TODO add warning for non-serializable (not str) timestr
            ...
        self.payload = payload
        if self.payload is ...:
            self.payload = {
                "count": self.count,
                "approxtime": self.timestr,
            }
        self.name = name
        if self.name is ...:
            self.name = f"Smg88 HeartBeat ({self.count}) at about {self.timestr}"
        if type(self.name) is not str:
            # TODO add warning for non-serializable (not str) name
            ...
        try:
            self._package = json.dumps(self.payload)
        except SafeCatchAll as err:
          # TODO properly handle this error :)
            ...
        super().__init__(channel=channel, name=name, payload=payload, **kwargs)


class EventStage():
    """Represents a place for events to occur
    Events are objects that have a channel and a name, all events are passed to all subscribers of that event's channel

    Events can be posted to this stage by instancing the 'Event' object and calling EventStageInstance.post(EventInstance)
    Or, shorthand, call 'send' on an Event instance with the EventStage instance

    Methods:
      subscribe(callback)
        Subscribes the function to be called with all Event objects posted to this stage under the channel (default __name__ of function)

    Attributes:
      nameHandle: str
        A common name for the EventStage, needed to connect to the EventStage
      subscriptions: Dict[str, Callable.__name__]
        Is a property exposing the subscriptions of the stage, the key is the channel and the value is the name of the subscriber's function

      _subscriptions: Dict[str, Callable]
        A dictionary of channel names to functions that are subscribed to that channel name
      _eventBuffer: List[Event]
        A buffer of events to post to the stage
    """
    _subscriptions: Dict[str, Callable] = ...
    nameHandle: str = ...

    _eventBuffer: List[Event] = ...

    @property
    def eventBuffer(self) -> List[Event]:
        return self._eventBuffer

    @property
    def channels(self) -> List[str]:
      return list(self._subscriptions.keys())

    def __init__(self, /, nameHandle: str = ...) -> None:
        self.nameHandle = nameHandle
        if self.nameHandle is ...:
            # TODO add warning for instinating an EventStage without a nameHandle
            ...
        if type(self.nameHandle) is not str:
            # TODO add warning for instinating an EventStage without a serializable (str) nameHandle
            ...
        self._subscriptions = {}
        self._eventBuffer = []

    def post(self, event: Event = ..., /, **kwargs) -> None:
        if event is ...:
            # TODO add warning for not passing an event
            raise errors.InappropriateRequest("No event was passed to the post method",
                                              errorHandle=errors.ProgrammerErrorHandle("Must pass an event to the post method"))
        self._eventBuffer.append(event)

    def release(self):
        self._post(num=1, all=False, retain=False)

    def subscribe(self, /, callback: Callable = ..., *, channel: str = ...) -> None:
      """Subscribes a callback to the given channel (defaults to callback.__name__)

      Args:
          callback (Callable): Callable to call with event=event when event is posted on that channel. Defaults to ....
          channel (str, optional): The exact channel to subscribe the callback to. Defaults to callback.__name__
      """
      # TODO add some info for this function as it is very useful
      if channel is ...:
        channel = callback.__name__
      print(f"Subscribing to EventStage {callback=} under {channel=}")
      if channel not in self.channels:
        self._subscriptions[channel] = []
      self._subscriptions[channel].append(callback)

    def _post(self, /, num: int = 1, *, all: bool = False, retain: bool = ..., **kwargs) -> None:
        if all:
            if retain is ...:
                retain = True
            if not retain:
                # TODO Warn for purging buffer
                ...
            self._postn(num=len(self._eventBuffer),
                        retain=bool(retain) ** kwargs)
        else:
            self._postn(num=num, retain=retain, **kwargs)

    def _postn(self, /, num: int = 1, *, retain: bool = False, **kwargs) -> None:
        for _ in range(num):
            self._handle(self._eventBuffer.pop(0))

    def _handle(self, event: Event) -> None:
        subscribers = [subscriber for channel, subscriber in self._subscriptions.items()
                       if channel == event.channel]
        subscribers = [subscriber]
        for subscriber in subscribers:
            try:
                subscriber(event=event)
            except SafeCatchAll as err:
                # TODO add warning for subscriber callback error
                raise err


class EventStageHeartbeat():
    """Represents a heartbeat for an AutoEventStage, subscribes to its own channel and reposts it with count++

    Attributes:
      SubscribeHandle: Callable
        Represents the handle 

    Methods:
      pump(): Pump this heartbeat once more!
      subscribe
    """

    counter: int = ...
    approxlastpump: str = ...

    stages: List[EventStage] = ...

    def __subscribeHandle(event: Event = ...) -> None:
        """Internal function to be called on a heartbeat

        Args:
            event (Event): Event to be analysed
        """
        print("Cool event handle called!")
        print(f"{event=}")

    def __init__(self, *, stage: EventStage = ..., stages: List[EventStage] = ..., countstart: int = -1) -> None:
        self.counter = countstart
        if type(self.counter) is not int:
            # TODO add warning for non-int counter
            raise errors.InappropriateRequest("counterstart must be an int", errorHandle=ProgrammerErrorHandle(
                "counterstart must be an int when instinating an EventStageHeartbeat object (or children of such)"))
        self.stages = []
        if stage is ... and stages is ...:
            # TODO add info for not passing a stage or stages
            ...
        if stage is not ... and stages is not ...:
            raise errors.InappropriateRequest("Cannot pass both a stage and stages", errorHandle=ProgrammerErrorHandle(
                "Please pass only a stages or a list of stages to an EventStageHeartbeat object constructor (or children thereof)"))
        if stage is ...:
            # TODO add info for not passing a stage
            ...
        else:
            self.stages.append(stage)
        if stages is ...:
            # TODO add info for not passing stages
            ...
        else:
            for stage in stages:
                self.stages.append(stage)

    def pump(self) -> None:
        self._step()

    def _step(self) -> None:
        self.counter += 1
        self.post()

    def post(self) -> None:
        [self.stage.post(event=HeartBeatEvent(count=self.counter,))
         for stage in self.stages]

    def _subscribeTo(self, *, stage: EventStage = ..., name: str = "Testing Name"):
        """Internal function to subscribe this heartbeat to an EventStage

        Args:
            stage (EventStage): Stage to subscribe to
        """
        if stage is ...:
            # TODO add error for calling _subscribeTo without a given stage
            raise errors.InappropriateRequest(
                "stage not given to _subscribeTo")

        @stage.subscribe
        @loghelp.callbacknamed(name)
        def _(event: Event = ...):
            self.__subscribeHandle()

    def setupStage(self, *, stage: EventStage = ...) -> None:
        """Setups up a stage to receive heartbeats from this object

        Args:
            stage (EventStage): Stage to setup (NOT a list of stages)
        """
        if stage is ...:
            # TODO add warning for calling setup without a stage
            raise errors.InappropriateRequest("stage not given to setupStage")
        self._subscribeTo(stage=stage)


class AutoEventStage(EventStage):
    """An EventStage that automatically posts its events (no manual post required)

    Args:
        nameHandle: str
        autosetup: bool
        heartbeat: EventStageHeartbeat
          Dependency injection
    """
    heartbeat: EventStageHeartbeat = ...

    def setup(self, *, heartbeat: EventStageHeartbeat = ...) -> None:
        if heartbeat is ...:
            self.heartbeat = EventStageHeartbeat()
        if type(self.heartbeat) is not EventStageHeartbeat:
            # TODO add warning for non-EventStageHeartbeat heartbeat
            ...
        self.heartbeat.subscribeTo(self)

        self.heartbeat.pump()

    def __init__(self, *, nameHandle: str = ..., autosetup: bool = True, heartbeat: EventStageHeartbeat = ...) -> None:
        super().__init__(nameHandle=nameHandle)
        self.heartbeat = heartbeat
        if self.heartbeat is ...:
            self.heartbeat = EventStageHeartbeat(stage=self, countstart=0)
        if autosetup:
            self.setup(heartbeat=self.heartbeat)


def main():
    stage = EventStage()

    @stage.subscribe
    @loghelp.callbacknamed("Smg88")
    def _(event: Event):
        print(f"EVENT {event=}")
    stage.post(Event(channel="Smg", name="help!", payload="TESTING!"))
    stage.post(Event(channel="Smg88", name="LETS F**KING GO!", payload="gout!"))
    stage._post(2)


if __name__ == "__main__":
    main()
