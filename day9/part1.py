import sys

def extrapolate_values(values):
    current_values = values
    sequences = [values]
    while any(current_values):
        sequence = [
            current_values[idx+1] - current_values[idx]
            for idx in range(len(current_values) - 1)
        ]
        sequences.append(sequence)
        current_values = sequence
    sequences = sequences[::-1]
    new_value = 0
    for idx in range(1, len(sequences)):
        new_value = sequences[idx][-1] + new_value
    return new_value



if __name__ == "__main__":
    for filename in sys.argv[1:]:
        lines = open(filename).read().splitlines()
        report = [list(map(int, line.split(" "))) for line in lines]
        extrapolated_values = [
            extrapolate_values(history)
            for history in report
        ]
        result = sum(extrapolated_values)
        print(f"Sum of extrapolated values is {result} in file {filename}")
