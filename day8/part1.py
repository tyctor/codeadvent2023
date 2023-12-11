import re
import sys

from itertools import cycle


node_re = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")

MOTION = {
    "L": 0,
    "R": 1,
}

def parse_network(lines):
    network = {}
    for line in lines:
        node, left, right = node_re.match(line).groups()
        network[node] = (left, right)
    return network


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        motion, nodes = open(filename).read().split("\n\n")
        lines = nodes.splitlines()
        network = parse_network(lines)

        position = network["AAA"]
        step = 0
        for direction in cycle(motion):
            idx = MOTION[direction]
            node_key = position[idx]
            position = network[node_key]
            step += 1
            if node_key == "ZZZ":
                break
        print(f"Steps from AAA to ZZZ is {step} in file {filename}")



