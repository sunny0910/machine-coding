from models.parkingFloor import ParkingFloor
from models.parkingSlot import ParkingSlot
from models.vehicleType import VehicleType
from models.ticket import Ticket


class ParkingLotService:
    slots_for_trucks = 1
    slots_for_bike = 2

    def __init__(self, lot_id, floors, slots_per_floor):
        self._id = lot_id
        self._total_floors = floors
        self._slots_per_floor = slots_per_floor
        self._parking_floors = []
        self.set_floors()
        self.ticket_id_to_slots = {}

    def get_id(self):
        return self._id

    def get_floors(self):
        return self._total_floors

    def get_slots_per_floor(self):
        return self._slots_per_floor

    def set_floors(self):
        for floor in range(self._total_floors):
            pf = ParkingFloor(floor+1)
            slots = []
            for i in range(self._slots_per_floor):
                if i < ParkingLotService.slots_for_trucks:
                    s = ParkingSlot(i+1, VehicleType.TRUCK.value, floor+1)
                elif i < ParkingLotService.slots_for_trucks + ParkingLotService.slots_for_bike:
                    s = ParkingSlot(i+1, VehicleType.BIKE.value, floor+1)
                else:
                    s = ParkingSlot(i+1, VehicleType.CAR.value, floor+1)
                slots.append(s)

            pf.set_slots(slots)
            self._parking_floors.append(pf)

    def park(self, vehicle):
        for i in range(len(self._parking_floors)):
            for j, slot in enumerate(self._parking_floors[i].slots):
                if slot.is_free and slot.get_vehicle_type() == vehicle.get_type():
                    slot_number = "%s_%s" % (self._id, self._parking_floors[i].slots[j].get_slot_number())
                    self._parking_floors[i].slots[j].set_vehicle(vehicle)
                    self._parking_floors[i].slots[j].is_free = False
                    vehicle.set_parking_slot(self._parking_floors[i].slots[j])
                    ticket = Ticket(slot_number, self._parking_floors[i].slots[j], vehicle)
                    self.ticket_id_to_slots[ticket.get_id()] = self._parking_floors[i].slots[j]
                    return ticket

        return None

    def unpark(self, ticket_id):
        slot = self.ticket_id_to_slots[ticket_id]
        del self.ticket_id_to_slots[ticket_id]
        slot.is_free = True
        # self._parking_floors[slot.get_floor()].slots[slot.get_id()].is_free = True
        vehicle = slot.get_vehicle()
        slot.set_vehicle(None)
        vehicle.set_parking_slot(None)
        return vehicle

    def display_free_count(self, vehicle_type):
        for i in range(len(self._parking_floors)):
            count = 0
            for slot in self._parking_floors[i].get_slots():
                if slot.is_free and slot.get_vehicle_type() == vehicle_type:
                    count += 1

            print("No. of free slots for %s on Floor %d: %d" % (vehicle_type, i+1, count))

    def display_free_slots(self, vehicle_type):
        for i in range(len(self._parking_floors)):
            slots = []
            for j, slot in enumerate(self._parking_floors[i].get_slots()):
                if slot.is_free and slot.get_vehicle_type() == vehicle_type:
                    slots.append(slot.get_id())

            print("Free slots for %s on Floor %d: %s" % (vehicle_type, i+1, ''.join(slots)))

    def display_occupied_slots(self, vehicle_type):
        for i in range(len(self._parking_floors)):
            slots = []
            for j, slot in enumerate(self._parking_floors[i].get_slots()):
                if not slot.is_free and slot.get_vehicle_type() == vehicle_type:
                    slots.append(str(slot.get_id()))

            print("Occupied slots for %s on Floor %d: %s" % (vehicle_type, i+1, ''.join(slots)))
