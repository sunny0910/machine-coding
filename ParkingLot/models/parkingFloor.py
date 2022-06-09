class ParkingFloor:
    def __init__(self, floor):
        self._floor = floor
        self.slots = None

    def get_floor(self):
        return self._floor

    def set_floor(self, floor):
        self._floor = floor

    def set_slots(self, slots):
        self.slots = slots

    def get_slots(self):
        return self.slots
