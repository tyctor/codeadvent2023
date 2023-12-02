import argparse
from game import Game
            

def main(args):
    for filename in args.file_names:
        file = open(filename).read()
        possible_games = []
        counts = {
            "red": args.num_of_red,
            "green": args.num_of_green,
            "blue": args.num_of_blue,
        }
        for line in file.splitlines():
            game = Game.parse_game(line)
            game_is_possible = game.is_possible(counts)
            possible_games.append(game_is_possible)
        result = sum(possible_games)
        print(f"Sum of possible games in file {filename} is {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process day2 from Advent of Code 2023.')
    parser.add_argument('file_names', type=str, nargs='+',
                        help='Files to process')
    parser.add_argument('--red', dest='num_of_red', action='store', required=True, type=int,
                        help='Number of red cubes')
    parser.add_argument('--blue', dest='num_of_blue', action='store', required=True, type=int,
                        help='Number of blue cubes')
    parser.add_argument('--green', dest='num_of_green', action='store', required=True, type=int,
                        help='Number of green cubes')

    args = parser.parse_args()
    main(args)

