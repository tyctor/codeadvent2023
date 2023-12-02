import argparse
import math
from game import Game
            

def main(args):
    for filename in args.file_names:
        file = open(filename).read()
        power_of_games = []
        for line in file.splitlines():
            game = Game.parse_game(line)
            minimum_set_of_cubes = game.minimum_set_of_cubes()
            power_of_games.append(math.prod(minimum_set_of_cubes.values()))
        result = sum(power_of_games)
        print(f"Sum of power of games in file {filename} is {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process day2 from Advent of Code 2023.')
    parser.add_argument('file_names', type=str, nargs='+',
                        help='Files to process')
    args = parser.parse_args()
    main(args)

