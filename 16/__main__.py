from math import ceil


def get_pattern(length, element_number):
    pattern = [0] * element_number
    pattern += [1] * element_number
    pattern += [0] * element_number
    pattern += [-1] * element_number
    if len(pattern) <= length + 1:
        pattern *= ceil((length + 1) / len(pattern))
    # Discard the very first value.
    return pattern[1:length + 1]


def apply_pattern(signal, pattern):
    assert len(signal) == len(pattern)
    value = sum([signal[i] * pattern[i] for i in range(len(signal))])
    # Keep only the ones digit.
    return abs(value) % 10


def do_phase(signal):
    length = len(signal)
    output = []
    for element_number in range(1, length + 1):
        pattern = get_pattern(length, element_number)
        output.append(apply_pattern(signal, pattern))
    return output


def fft(signal, phases):
    for _ in range(phases):
        signal = do_phase(signal)
    return signal


with open("16/input.txt") as f:
    input_string = f.readline().strip()
input_signal = [int(c) for c in input_string]
output = fft(input_signal, 100)
print(f"The answer to Part 1 is {''.join(map(str, output[:8]))}.")
