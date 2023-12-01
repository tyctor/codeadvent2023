import sys

def get_calibration_value(line):
    position_of_digits = [(i, int(c)) for i, c in enumerate(line) if c.isdigit()]
    position_of_words = []
    last_digit_len = 0
    for i, digit in enumerate(digits, start=1):
        pos = line.find(digit)
        while pos > -1:
            position_of_words.append((pos, i, digit))
            pos = line.find(digit, pos + 1)
    if len(position_of_digits) == 0 and len(position_of_words) == 0:
        print(f"No number/digit found in line `{line}`")
        return 0
    min_from_digits = min(position_of_digits, default=(len(line) + 1, 0), key = lambda t: t[0])
    max_from_digits = max(position_of_digits, default=(-1, 0, "zero"), key = lambda t: t[0])
    min_from_words = min(position_of_words, default=(len(line) + 1, 0), key = lambda t: t[0])
    max_from_words = max(position_of_words, default=(-1, 0, "zero"), key = lambda t: t[0])
    min_from_both = min(min_from_digits, min_from_words, key = lambda t: t[0])
    max_from_both = max(max_from_digits, max_from_words, key = lambda t: t[0])
    return int(f"{min_from_both[1]}{max_from_both[1]}")


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        file = open(filename)
        digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        calibration_values = []
        for line in file.readlines():
            calibration_value = get_calibration_value(line)
            calibration_values.append(calibration_value)
        result = sum(calibration_values)
        print(f"Sum of calibration values in file {filename} is {result}")
