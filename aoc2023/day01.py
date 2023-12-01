import re

digits_map = [["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"],
              ["eight", "8"], ["nine", "9"], ["zero", "0"]]


def convert_to_digits(line: str):
    result = ""
    for i in range(0, len(line)):
        result += get_next_digit(line[i:len(line):1])
    return result


def get_next_digit(line: str):
    for digit in digits_map:
        if line.startswith(digit[0]) or line.startswith(digit[1]):
            return digit[1]
    return ""


def part_one():
    total = 0
    with open("inputs/day01.txt") as f:
        for line in f:
            digits = re.findall("\\d", line)
            first = digits[0]
            last = digits[len(digits) - 1]
            total += int(first + last)
        return total


def part_two():
    total = 0
    with open("inputs/day01.txt") as f:
        for line in f:
            digits_line = convert_to_digits(line)
            digits = re.findall("\\d", digits_line)
            first = digits[0]
            last = digits[len(digits) - 1]
            total += int(first + last)
        return total


print("Part 1:", part_one())
print("Part 2:", part_two())
