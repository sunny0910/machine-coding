class Board:
    def __init__(self, size):
        self.size = size
        self.snakes = []
        self.ladders = []
        self.player_positions = {}
        self.snakes_map = None
        self.ladders_map = None

    def get_size(self):
        return self.size

    def set_snakes(self, snakes):
        self.snakes = snakes

    def set_ladders(self, ladders):
        self.ladders = ladders

    def set_player_positions(self, player_positions):
        self.player_positions = player_positions

    def set_snakes_and_ladder_map(self):
        self.snakes_map = {}
        for snake in self.snakes:
            self.snakes_map[snake.head] = snake.tail

        self.ladders_map = {}
        for ladder in self.ladders:
            self.ladders_map[ladder.start] = ladder.end
