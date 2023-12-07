import re

numbers = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    r"\d",
)

digits_re = re.compile("(?=(" + "|".join(numbers) + "))")

total = 0

with open("day_1/input.txt") as f:
    lines = f.readlines()

for line in lines:
    digits = digits_re.findall(line)

    this = ""
    for digit in (digits[0], digits[-1]):
        this += str(numbers.index(digit)) if digit in numbers else digit

    total += int(this)

print(total)
