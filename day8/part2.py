import math
import re
import sys

from itertools import cycle


node_re = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")

MOTION = {
    "L": 0,
    "R": 1,
}


def find_prime_factors(n):
    factorlist = []
    num = n
    while (n % 2 == 0):
        factorlist.append(2)
        n = n/2
    for i in range(3,int(num/2)+1,2):
        while (n % i == 0):
            factorlist.append(i)
            n = n/i
        if (n==1):
            break
    return(factorlist)


def parse_network(lines):
    network = {}
    start_nodes = []
    for line in lines:
        node, left, right = node_re.match(line).groups()
        network[node] = (left, right)
        if node[-1] == "A":
            start_nodes.append(node)
    return network, start_nodes


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        motion, nodes = open(filename).read().split("\n\n")
        lines = nodes.splitlines()
        network, start_nodes = parse_network(lines)

        positions = [network[node] for node in start_nodes]
        steps_per_node = {}

        for node in start_nodes:
            position = network[node]
            step = 0
            for direction in cycle(motion):
                idx = MOTION[direction]
                node_key = position[idx]
                position = network[node_key]
                step += 1
                if node_key[-1] == "Z":
                    break
            steps_per_node[node] = step
        node_prime_factors = {}
        for node, steps in steps_per_node.items():
            node_prime_factors[node] = find_prime_factors(steps)
        commom_prime_factors = set()
        for prime_factors in node_prime_factors.values():
            for num in prime_factors:
                commom_prime_factors.add(num)
        result = math.prod(commom_prime_factors)
        print(f"Steps from *A to *Z is {result} in file {filename}")

