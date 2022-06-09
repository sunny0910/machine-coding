from services.snakesAndLaddersService import SnakesAndLadderService
from models import snake, ladder, player, board


class Game:
    def __init__(self, file_name):
        self.file_name = file_name
        self.board_size = 0
        self.snakes = []
        self.ladders = []
        self.players = []
        pass

    def main(self):
        self.read_input()
        self.start_game()

    def read_input(self):
        with open(self.file_name) as input_file:
            self.board_size = int(input_file.readline()[:-1])
            number_of_snakes = input_file.readline()[:-1]
            for i in range(int(number_of_snakes)):
                line = input_file.readline()
                line = line[:-1]
                line = line.split(" ")
                line = list(map(int, line))
                if not snake.Snake.validate_snake(line[0], line[1], self.board_size):
                    raise ValueError("Error in snake values i: ", i)
                s = snake.Snake(line[0], line[1])
                self.snakes.append(s)

            number_of_ladders = input_file.readline()[:-1]
            for i in range(int(number_of_ladders)):
                line = input_file.readline()
                line = line[:-1].split(" ")
                line = list(map(int, line))
                lad = ladder.Ladder(line[0], line[1])
                if not ladder.Ladder.validate_ladder(line[0], line[1], self.board_size):
                    raise ValueError(Exception("Error in ladder value i:", i))
                self.ladders.append(lad)

            number_of_players = input_file.readline()
            for i in range(int(number_of_players)):
                line = input_file.readline()
                line = line[:-1]
                p = player.Player(line)
                self.players.append(p)

    def start_game(self):
        game_service = SnakesAndLadderService()
        game_service.set_board(self.board_size)
        game_service.set_players(self.players)
        game_service.set_ladders(self.ladders)
        game_service.set_snakes(self.snakes)
        game_service.board.set_snakes_and_ladder_map()
        game_service.start_game()


if __name__ == '__main__':
    file = 'input.txt'
    g = Game(file)
    g.main()
