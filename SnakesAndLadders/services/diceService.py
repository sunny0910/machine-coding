import random


class DiceService:

    def __init__(self, dices_num):
        self.number_of_dices = dices_num

    @staticmethod
    def roll():
        return random.randrange(1, 6)
