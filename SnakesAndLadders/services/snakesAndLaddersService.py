from collections import deque
from models.board import Board
from services.diceService import DiceService


class SnakesAndLadderService:
    default_dice = 1
    default_board_size = 100

    def __init__(self):
        self.diceService = DiceService(SnakesAndLadderService.default_dice)
        self.players = []
        self.player_queue = deque([])
        self.number_of_players = 0
        self.board = None
        self.is_game_completed = False
        self.should_game_continue_till_last_player = False
        self.should_allow_multiple_rolls_after_six = False

    def set_board(self, size=None):
        self.board = Board(size if size else SnakesAndLadderService.default_board_size)

    def set_players(self, players):
        self.number_of_players = len(players)
        self.players = players
        self.player_queue = deque([], maxlen=self.number_of_players)
        player_positions = {}
        for p in self.players:
            self.player_queue.append(p)
            player_positions[p.get_id()] = 0

        self.board.set_player_positions(player_positions)

    def set_snakes(self, snakes):
        self.board.set_snakes(snakes)

    def set_ladders(self, ladders):
        self.board.set_ladders(ladders)

    def start_game(self):
        while not self.game_completed():
            dice_value = self.dice_roll()
            player = self.player_queue.popleft()
            self.move_player(player, dice_value)
            if self.player_won(self.board.player_positions[player.id]):
                print("Player %s has won" % player.name)
                del self.board.player_positions[player.id]
            else:
                self.player_queue.append(player)

    def move_player(self, player, dice_value):
        curr_position = self.board.player_positions[player.id]
        new_position = curr_position + dice_value
        if new_position > self.board.size:
            new_position = curr_position
        else:
            new_position = self.get_new_position_after_snakes_ladders(new_position)

        self.board.player_positions[player.id] = new_position
        print("Player %s moved from %d to %d" % (player.name, curr_position, new_position))

    def get_new_position_after_snakes_ladders(self, new_position):
        while new_position in self.board.snakes_map and new_position in self.board.ladders_map:
            if new_position in self.board.snakes_map:
                new_position = self.board.snakes_map[new_position]

            if new_position in self.board.ladders_map:
                new_position = self.board.ladders_map[new_position]
        return new_position

    def player_won(self, position):
        return position == self.board.get_size()

    def game_completed(self):
        if len(self.player_queue) > 1:
            return False

        return True

    def dice_roll(self):
        return self.diceService.roll()
