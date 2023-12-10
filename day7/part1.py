import sys


CARDS = "23456789TJQKA"



def parse_hands(lines):
    hands = [line.split(" ") for line in lines]
    return list(map(lambda h: (h[0], int(h[1])), hands))


def score(hand):
    strong = tuple(CARDS.find(r) for r in hand)
    rcounts = {CARDS.find(r): hand.count(r) for r in hand}.items()
    score, ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
    return score, strong, ranks


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        lines = open(filename).read().splitlines()
        hands = parse_hands(lines)
        scores = [(i, score(hand[0]), hand[0], hand[1]) for i, hand in enumerate(hands)]
        ordered_by_score = sorted(scores, key=lambda x: x[1])
        result = sum([idx * bid for idx, (order, score_ranks, hand, bid) in enumerate(ordered_by_score, start=1)])
        print(f"Total winning is {result} in file {filename}")
