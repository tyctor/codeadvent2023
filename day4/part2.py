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
        all_cards = {}
        for card, line in enumerate(file.splitlines(), start=1):
            cards = all_cards.setdefault(card, {"original": [], "copy": []})
            cards["original"].append(card)
            numbers = parse_card_numbers(line)
            winning_numbers = find_winning_numbers(**numbers)
            if winning_numbers:
                for _ in range(len(all_cards[card]["copy"]) + 1):
                    for win_card in range(card + 1, len(winning_numbers) + card + 1):
                        cards = all_cards.setdefault(win_card, {"original": [], "copy": []})
                        cards["copy"].append(win_card)
        result = sum(map(lambda c: len(c["copy"]) + 1, all_cards.values()))
        print(f"At the end we have {result} cards in file {filename}")
