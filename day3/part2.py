import sys
import math


def is_valid_symbol(symbol):
    return symbol == "*"


def has_adjacent_symbol(row, col_from, col_to, engine):
    for col in range(col_from, col_to + 1):
        if is_valid_symbol(engine[row][col]):
            return True, row, col
    return False, -1, -1


def has_adjacent_symbol_around(row, col_from, col_to, last_row, last_col, engine):
    # left
    if col_from > 0:
        col_from -= 1
        if is_valid_symbol(engine[row][col_from]):
            return True, row, col_from
    # right
    if col_to < last_col:
        if is_valid_symbol(engine[row][col_to]):
            return True, row, col_to
    # top
    if row > 0:
        result = has_adjacent_symbol(row-1, col_from, col_to, engine)
        if result[0]:
            return result
    # bottom 
    if row < last_row:
        result = has_adjacent_symbol(row+1, col_from, col_to, engine)
        if result[0]:
            return result
    return False, -1, -1

 
if __name__ == "__main__":
    for filename in sys.argv[1:]:
        file = open(filename).read()
        engine = []
        gear_parts = {}
        # read engine
        for line in file.splitlines():
            row = []
            for char in line:
                row.append(char) 
            engine.append(row)
        # traverse engine
        last_row = len(engine) - 1
        last_col = len(engine[0]) - 1
        for row in range(len(engine)):
            part_number_started = False
            part_number_col_from = 0
            part_number_col_to = 0
            digits = []
            for col in range(len(engine[row])):
                symbol = engine[row][col]
                if symbol.isdigit():
                    if not part_number_started:
                        part_number_started = True
                        part_number_col_from = col
                    digits.append(symbol)
                elif part_number_started:
                    part_number_started = False
                    part_number_col_to = col
                    result = has_adjacent_symbol_around(row, part_number_col_from, part_number_col_to, last_row, last_col, engine)
                    if result[0]:
                        part_number = int(''.join(digits))
                        gear_numbers = gear_parts.setdefault(tuple(result[1:]), [])
                        gear_numbers.append(part_number)
                    digits = []
                if digits and col == last_col:
                    part_number_col_to = col
                    result = has_adjacent_symbol_around(row, part_number_col_from, part_number_col_to, last_row, last_col, engine)
                    if result[0]:
                        part_number = int(''.join(digits))
                        gear_numbers = gear_parts.setdefault(tuple(result[1:]), [])
                        gear_numbers.append(part_number)
        # accept gears with exactly two parts
        gear_parts = {pos: math.prod(parts) for pos, parts in gear_parts.items() if len(parts) == 2}
        result = sum(gear_parts.values())
        print(f"Sum of gear ratios in file {filename} is {result}")

