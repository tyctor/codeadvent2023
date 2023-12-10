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


def parse_seed_ranges(line):
    _, numbers = line.split(": ")
    numbers = parse_numbers(numbers)
    return [(numbers[idx], numbers[idx+1]) for idx in range(0, len(numbers), 2)]


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


def find_min_location(seed_range, ranges):
    start, length = seed_range
    location = None
    for seed in range(start, start + length):
        current = find_location(seed, ranges)
        if not location or location > current:
            location = current
    return location



if __name__ == "__main__":
    for filename in sys.argv[1:]:
        sections = open(filename).read().split("\n\n")
        SEEDS = parse_seed_ranges(sections.pop(0))
        for section_str in sections:
            lines = section_str.splitlines()
            current_section = SECTIONS[lines.pop(0)]
            parse_map_ranges(current_section, lines)
        locations = {}
        with concurrent.futures.ProcessPoolExecutor(max_workers=7) as executor:
            seed_to_location = {
                executor.submit(find_min_location, seed_range, list(SECTIONS.values())): seed_range for idx, seed_range in enumerate(SEEDS, start=1)
            }
            for future in concurrent.futures.as_completed(seed_to_location):
                seed_range = seed_to_location[future]
                try:
                    location = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (seed_range, exc))
                else:
                    locations[seed_range] = location
        result = min(locations.values())
        print(f"Lowest location number is {result} in file {filename}")
