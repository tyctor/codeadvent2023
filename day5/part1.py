import concurrent.futures
import sys
from operator import itemgetter

SEED = "seed"
SOIL = "soil"
FERTILIZER = "fertilizer"
WATER = "water"
LIGHT = "light"
TEMPERATURE = "temperature"
HUMIDITY = "humidity"
LOCATION = "location"

SECTIONS = {
    f"{SEED}-to-{SOIL} map:": [],
    f"{SOIL}-to-{FERTILIZER} map:": [],
    f"{FERTILIZER}-to-{WATER} map:": [],
    f"{WATER}-to-{LIGHT} map:": [],
    f"{LIGHT}-to-{TEMPERATURE} map:": [],
    f"{TEMPERATURE}-to-{HUMIDITY} map:": [],
    f"{HUMIDITY}-to-{LOCATION} map:": [],
}


def parse_numbers(numbers):
    return list(map(int, numbers.split(" ")))


def parse_seed_numbers(line):
    _, numbers = line.split(": ")
    return parse_numbers(numbers)


def parse_map_ranges(ranges, section_lines):
    for line in section_lines:
        ranges.append(parse_numbers(line))
    ranges.sort(key=itemgetter(1))


def get_mapping(seed, ranges):
    for dest, src, range_len in ranges:
        if src <= seed < src + range_len:
            shift = seed - src
            return dest + shift
    return seed


def find_location(seed, ranges):
    current = seed
    for section in ranges:
        current = get_mapping(current, section)
    return current


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        sections = open(filename).read().split("\n\n")
        SEEDS = parse_seed_numbers(sections.pop(0))
        for section_str in sections:
            lines = section_str.splitlines()
            current_section = SECTIONS[lines.pop(0)]
            parse_map_ranges(current_section, lines)
        locations = {}
        for seed in SEEDS:
            location = find_location(seed, SECTIONS.values())
            locations[seed] = location
        result = min(locations.values())
        print(f"Lowest location number is {result} in file {filename}")
