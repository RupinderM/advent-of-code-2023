import re

with open("input") as file:
    data = file.readlines()

result = 0

for line in data:
    all_numbers = re.findall("\d+", line)
    matches = len(set(all_numbers[1:11]).intersection(set(all_numbers[11:])))
    if matches:
        result += 2 ** (matches - 1)

print(result)
