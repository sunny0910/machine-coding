class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    @staticmethod
    def validate_ladder(start, end, board_size):
        if start < board_size and board_size > end > start:
            return True

        return False
