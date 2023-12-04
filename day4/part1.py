import re
import sys

card_re = re.compile(r"Card\s+\d+:\s+(?P<winning_numbers>[^|]+)\|(?P<my_numbers>.+)$")
card_number_re = re.compile(r"\d+")


def find_winning_numbers(winning_numbers, my_numbers):
    return [number for number in my_numbers if number in winning_numbers]


def parse_card_numbers(line):
    output = {}
    for group, numbers in card_re.match(line).groupdict().items():
        output[group] = re.findall(card_number_re, numbers)
    return output


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        file = open(filename).read()
        points_from_cards = []
        for line in file.splitlines():
            numbers = parse_card_numbers(line)
            winning_numbers = find_winning_numbers(**numbers)
            if winning_numbers:
                points_from_cards.append(2**(len(winning_numbers)-1))
        result = sum(points_from_cards)
        print(f"Total points from cards in file {filename} is {result}")
