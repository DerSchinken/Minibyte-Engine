from typing import Callable
from tkinter import Event

from src.core.display.Canvas import Canvas
from src.core.display.Window import Window


class InputEvent:
    """
    Basic event handler

    events - Shared class variable (each subclass will have their own shared events variable)
    """
    events = {}

    def __init__(self, parent: Window | Canvas):
        self.parent = parent

    def call_events(self, event_name: str, event: Event) -> None:
        """
        Used since in normal tkinter .unbind you can only unset all function from an event
        :param event_name: Event name
        :param event: event object
        :return:
        """
        for func in self.events[event_name]:
            func(event)

    def add_event(self, event_name: str, func: Callable) -> None:
        """
        :param event_name: Event name
        :param func: Function that will be called when event triggers
        :return:
        """
        self.__setitem__(event_name, func)

    def remove_event_function(self, func: Callable, event_name: str = None) -> None:
        """
        :param func: function that shall be removed
        :param event_name: Event name (optional if not given then func will be removed from all events)
        :return:
        """
        try:
            if event_name:
                self.events[event_name] = self.events[event_name].remove(func)
                if len(self.events[event_name]) < 1:
                    self.parent.unbind(event_name)
            else:
                for event in self.events.keys():
                    self.events[event].remove(func)
                    if len(self.events[event]) < 1:
                        self.parent.unbind(event)
        except ValueError:
            pass

    def __setitem__(self, key: str, value: Callable):
        if self.events.get(key):
            # NOTE: ^ Could maybe cause trouble for example when list is not empty but event is unbound
            self.events[key].append(value)
        else:
            self.events[key] = [value]
            self.parent.bind(key, lambda e: self.call_events(key, e))
            # self.parent.bind(key, value)
            # ^ Using custom solution since you can't unbind specific event functions

    def __getitem__(self, item: str) -> Callable:
        return self.events[item]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.events = {}
