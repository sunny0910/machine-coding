class Ticket:
    def __init__(self, ticket_id, slot, vehicle):
        self._ticket_id = ticket_id
        self._parking_slot = slot
        self._vehicle = vehicle

    def get_id(self):
        return self._ticket_id

    def get_parking_slot(self):
        return self._parking_slot

    def get_vehicle(self):
        return self._vehicle