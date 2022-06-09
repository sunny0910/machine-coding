class Vehicle:
    def __init__(self, vehicle_type, number, color, parking_slot):
        self._type = vehicle_type
        self._registration_number = number
        self._color = color
        self._parking_slot = parking_slot

    def set_parking_slot(self, slot):
        self._parking_slot = slot

    def get_parking_slot(self):
        return self._parking_slot

    def set_color(self, color):
        self._color = color
        return

    def get_color(self):
        return self._color

    def set_type(self, vehicle_type):
        self._type = vehicle_type

    def get_type(self):
        return self._type

    def set_number(self, number):
        self._registration_number = number

    def get_number(self):
        return self._registration_number
