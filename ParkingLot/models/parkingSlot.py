class ParkingSlot:
    def __init__(self, slot_id, vehicle_type, floor):
        self._id = slot_id
        self._vehicle = None
        self._vehicle_type = vehicle_type
        self.is_free = True
        self._floor = floor

    def get_vehicle(self):
        return self._vehicle

    def set_vehicle(self, vehicle):
        self._vehicle = vehicle

    def set_vehicle_type(self, vehicle_type):
        self._vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self._vehicle_type

    def set_floor(self, floor):
        self._floor = floor

    def get_floor(self):
        return self._floor

    def set_id(self, slot_id):
        self._id = slot_id

    def get_id(self):
        return self._id

    def get_slot_number(self):
        return "%s_%s" % (self._floor, self._id)
