import sys

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        calibration_values = []
        file = open(filename).read()
        for line in file.splitlines():
            position_of_digits = [(i, int(c)) for i, c in enumerate(line) if c.isdigit()]
            if len(position_of_digits) == 0:
                print(f"No number found in line `{line}`")
                continue
            if len(position_of_digits) == 1:
                position_of_digits.append(position_of_digits[0])
            calibration_value = int(f"{position_of_digits[0][1]}{position_of_digits[-1][1]}")
            calibration_values.append(calibration_value)
        result = sum(calibration_values)
        print(f"Sum of calibration values in file {filename} is {result}")
