from enum import Enum


class ParkingLotCommands(Enum):
    create = 'create_parking_lot'
    display = 'display'
    park = 'park_vehicle'
    unpark = 'unpark_vehicle'
    exit = 'exit'
