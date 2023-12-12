import sys
import numpy as np


def parse_space(lines):
    space = []
    galaxy_counter = 1
    for line in lines:
        row = []
        for point in line:
            if point == ".":
                row.append(0)
            elif point == "#":
                row.append(galaxy_counter)
                galaxy_counter += 1
        space.append(row)
    return space


def expand_space(space):
    array = np.array(space)
    row_to_expand = np.where(~array.any(axis=1))[0]
    cols_to_expand = np.where(~array.any(axis=0))[0]
    for col in reversed(cols_to_expand):
        array = np.insert(array, col, 0, axis=1)
    for row in reversed(row_to_expand):
        array = np.insert(array, row, 0, axis=0)
    return array


def get_shortest_paths(galaxies):
    idx = 0
    for galaxy_from in galaxies:
        for galaxy_to in galaxies[idx:]:
            if galaxy_from != galaxy_to:
                yield abs(galaxy_to[0] - galaxy_from[0]) + abs(galaxy_to[1] - galaxy_from[1])
        idx += 1



if __name__ == "__main__":
    for filename in sys.argv[1:]:
        lines = open(filename).read().splitlines()
        space = parse_space(lines)
        expanded = expand_space(space)
        galaxies = list(zip(*np.nonzero(expanded)))
        sum_of_lengths = sum(get_shortest_paths(galaxies))
        print(f"Sum of legths is {sum_of_lengths} in file {filename}")

