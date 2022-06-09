from services.parkingLot import ParkingLotService
from models.commands import ParkingLotCommands
from models.vehicle import Vehicle
from models.display_type import DisplayType


class Driver:
    def __init__(self):
        self.parking_lot = None

    def run(self):
        while True:
            command = input()
            commands = command.split(" ")
            command_type = commands[0]

            if command_type == ParkingLotCommands.create.value:
                if self.parking_lot:
                    print("parking lot already defined")
                else:
                    lot_id, floors, slots_per_floor = commands[1], int(commands[2]), int(commands[3])
                    self.parking_lot = ParkingLotService(lot_id, floors, slots_per_floor)
                    print("parking lot created with %d floors and %d slots on each floor" % (floors, slots_per_floor))

            elif command_type == ParkingLotCommands.display.value:
                if not self.parking_lot:
                    print("no parking lot defined")
                else:
                    sub_command, vehicle_type = commands[1], commands[2]
                    if sub_command == DisplayType.FREE_COUNT.value:
                        self.parking_lot.display_free_count(vehicle_type)
                    elif sub_command == DisplayType.FREE_SLOTS.value:
                        self.parking_lot.display_free_slots(vehicle_type)
                    elif sub_command == DisplayType.OCCUPIED_SLOTS.value:
                        self.parking_lot.display_occupied_slots(vehicle_type)
                    else:
                        print("invalid display type")

            elif command_type == ParkingLotCommands.park.value:
                if not self.parking_lot:
                    print("no parking lot defined")
                else:
                    vehicle_type = commands[1]
                    vehicle_number = commands[2]
                    color = commands[3]
                    v = Vehicle(vehicle_type, vehicle_number, color, None)
                    ticket = self.parking_lot.park(v)
                    if not ticket:
                        print("parking lot full")
                    else:
                        print("Parked Vehicle. Ticket ID: %s" % ticket.get_id())

            elif command_type == ParkingLotCommands.unpark.value:
                if not self.parking_lot:
                    print("no parking lot defined")
                else:
                    ticket_id = commands[1]
                    vehicle = self.parking_lot.unpark(ticket_id)
                    print("Unparked vehicle with Registration Number: %s and Color: %s" % (vehicle.get_number(),
                                                                                           vehicle.get_color()))
            elif command_type == ParkingLotCommands.exit.value:
                break
            else:
                print("Invalid command")


if __name__ == '__main__':
    d = Driver()
    d.run()
