import math
import re
import sys


number_re = re.compile(r"\d+")

def parse_numbers(numbers):
    return list(map(int, re.findall(number_re, numbers)))


def find_better_races(race_time, best_distance):
    better_races = []
    for charging in range(race_time):
        moving = race_time - charging
        distance = moving * charging
        if distance > best_distance:
            better_races.append(distance)
    return better_races


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        time_line, distance_line = open(filename).read().splitlines()
        race_times = parse_numbers(time_line.replace(" ", ""))
        distances = parse_numbers(distance_line.replace(" ", ""))
        races = []
        for race_time, best_distance in zip(race_times, distances):
            races.append(find_better_races(race_time, best_distance))
        result = math.prod(map(len, races))
        print(f"Result number is {result} in file {filename}")
