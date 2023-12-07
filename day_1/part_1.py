import re

digits_re = re.compile(r"\D")

total = 0

with open("day_1/input.txt") as f:
    lines = f.readlines()

for line in lines:
    digits = digits_re.sub("", line)
    total += int(digits[0] + digits[-1])

print(total)
