import uuid


class Player:
    def __init__(self, name):
        self.id = uuid.uuid1()
        self.name = name
        self.rank = 0
        self.current_position = 0

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_current_position(self):
        return self.current_position

    def set_current_position(self, pos):
        self.current_position = pos

    def set_rank(self, rank):
        self.rank = rank

    def get_rank(self):
        return self.rank

