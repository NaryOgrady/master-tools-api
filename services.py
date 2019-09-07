from db import get_session, TravelEvent


class TravelEventService:
    data = None

    def __init__(self):
        if TravelEventService.data is None:
            TravelEventService.data = TravelEventService.get_data()

    @staticmethod
    def get_data():
        session = get_session()
        return session.query(TravelEvent)

    def get_travel_event(self):
        return self.data[2]
