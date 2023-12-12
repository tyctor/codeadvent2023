import sys

# The pipes are arranged in a two-dimensional grid of tiles:
#
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

NS = "|"
EW = "-"
NE = "L"
NW = "J"
SW = "7"
SE = "F"
GND = "."
START = "S"

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"

POSSIBLE_CONNECTIONS = {
    NS: [SOUTH, NORTH],
    EW: [WEST, EAST],
    NE: [SOUTH, WEST],
    NW: [SOUTH, EAST],
    SW: [NORTH, EAST],
    SE: [NORTH, WEST],
}

DIRECTIONS = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    EAST: (0, 1),
    WEST: (0, -1),
}


def parse_maze(lines):
    maze = []
    start = None
    for ridx, line in enumerate(lines):
        row = []
        for cidx, point in enumerate(line):
            row.append(point)
            if point == START:
                start = (ridx, cidx)
        maze.append(row)
    return maze, start


def possible_direction(maze, start):
    row, col = start
    for direction, (dir_y, dir_x) in DIRECTIONS.items():
        pos_y = row + dir_y
        pos_x = col + dir_x
        pipe = maze[pos_y][pos_x]
        if pipe == GND:
            continue
        possible_dirs = POSSIBLE_CONNECTIONS[pipe]
        if direction in possible_dirs:
            return direction


def direction_from_pos(pipe, going_to):
    if going_to == NORTH:
        if pipe == NS:
            return NORTH
        elif pipe == SE:
            return EAST
        elif pipe == SW:
            return WEST
    elif going_to == SOUTH:
        if pipe == NS:
            return SOUTH
        elif pipe == NE:
            return EAST
        elif pipe == NW:
            return WEST
    elif going_to == EAST:
        if pipe == EW:
            return EAST
        elif pipe == NW:
            return NORTH
        elif pipe == SW:
            return SOUTH
    elif going_to == WEST:
        if pipe == EW:
            return WEST
        elif pipe == NE:
            return NORTH
        elif pipe == SE:
            return SOUTH


def find_distance(maze, start, direction):
    pos_y, pos_x = start
    pipe = None
    distance = 0
    while pipe != START:
        dir_y, dir_x = DIRECTIONS[direction]
        pos_y += dir_y
        pos_x += dir_x
        distance += 1
        pipe = maze[pos_y][pos_x]
        if pipe != START:
            direction = direction_from_pos(pipe, direction)
    return distance


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        lines = open(filename).read().splitlines()
        maze, start = parse_maze(lines)
        direction = possible_direction(maze, start)
        distance = find_distance(maze, start, direction)
        print(f"Distance to {direction} is {int(distance/2)} in file {filename}")
