class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def set_head(self, head):
        self.head = head

    def set_tail(self, tail):
        self.tail = tail

    def get_head(self):
        return self.tail

    def get_tail(self):
        return self.tail

    @staticmethod
    def validate_snake(head, tail, board_size):
        if tail < head and board_size > head > tail:
            return True

        return False
