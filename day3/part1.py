import sys


def is_valid_symbol(symbol):
    return not (symbol.isdigit() or symbol == ".")


def has_adjacent_symbol(row, col_from, col_to, engine):
    for col in range(col_from, col_to + 1):
        if is_valid_symbol(engine[row][col]):
            return True
    return False


def has_adjacent_symbol_around(row, col_from, col_to, last_row, last_col, engine):
    # left
    if col_from > 0:
        col_from -= 1
        if is_valid_symbol(engine[row][col_from]):
            return True
    # right
    if col_to < last_col:
        if is_valid_symbol(engine[row][col_to]):
            return True
    # top
    if row > 0:
        if has_adjacent_symbol(row-1, col_from, col_to, engine):
            return True
    # bottom 
    if row < last_row:
        if has_adjacent_symbol(row+1, col_from, col_to, engine):
            return True
    return False

 
if __name__ == "__main__":
    for filename in sys.argv[1:]:
        file = open(filename).read()
        engine = []
        part_numbers = []
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
                    if has_adjacent_symbol_around(row, part_number_col_from, part_number_col_to, last_row, last_col, engine):
                        part_number = int(''.join(digits))
                        part_numbers.append(part_number)
                    digits = []
                if digits and col == last_col:
                    part_number_col_to = col
                    if has_adjacent_symbol_around(row, part_number_col_from, part_number_col_to, last_row, last_col, engine):
                        part_number = int(''.join(digits))
                        part_numbers.append(part_number)
        result = sum(part_numbers)
        print(f"Sum of part number values in file {filename} is {result}")

