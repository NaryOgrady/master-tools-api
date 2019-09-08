import random
from db import get_session, TravelEvent


class TravelEventService:
    events = None
    options = ['morning', 'afternoon', 'night']

    def __init__(self):
        if TravelEventService.events is None:
            TravelEventService.events = TravelEventService.get_data()

    @staticmethod
    def get_data():
        session = get_session()
        data = {}
        for option in TravelEventService.options:
            data[option] = [events for events in session.query(
                TravelEvent).filter(TravelEvent.option == option)]
        return data

    def get_travel_events(self):
        roll = random.randint(1, 100)
        data = {}
        for option in self.options:
            data[option] = [event for event in self.events[option]
                            if roll >= event.low and roll <= event.high][0]
        return data
