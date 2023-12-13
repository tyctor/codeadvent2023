import sys
import numpy as np


EXPAND_BY = 1000000

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
    rows_to_expand = np.where(~array.any(axis=1))[0]
    cols_to_expand = np.where(~array.any(axis=0))[0]
    return array, rows_to_expand, cols_to_expand


def get_expanded(row_from, row_to, rows_to_expand, col_from, col_to, cols_to_expand):
    if row_from > row_to:
        row_from, row_to = row_to, row_from
    if col_from > col_to:
        col_from, col_to = col_to, col_from
    expanded_rows = []
    for row in rows_to_expand:
        if row_from < row < row_to:
            expanded_rows.append(row)
    expanded_cols = []
    for col in cols_to_expand:
        if col_from < col < col_to:
            expanded_cols.append(col)
    return row_to + ((EXPAND_BY - 1) * len(expanded_rows)) - row_from + col_to + ((EXPAND_BY - 1) * len(expanded_cols)) - col_from


def get_shortest_paths(galaxies, rows_to_expand, cols_to_expand):
    idx = 0
    for galaxy_from in galaxies:
        for galaxy_to in galaxies[idx:]:
            if galaxy_from != galaxy_to:
                yield get_expanded(galaxy_to[0], galaxy_from[0], rows_to_expand, galaxy_to[1], galaxy_from[1], cols_to_expand)
        idx += 1



if __name__ == "__main__":
    for filename in sys.argv[1:]:
        lines = open(filename).read().splitlines()
        space = parse_space(lines)
        space, rows_to_expand, cols_to_expand = expand_space(space)
        galaxies = list(zip(*np.nonzero(space)))
        paths = list(get_shortest_paths(galaxies, rows_to_expand, cols_to_expand))
        sum_of_lengths = sum(paths)
        print(f"Sum of legths is {sum_of_lengths} in file {filename}")

