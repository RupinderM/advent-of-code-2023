import re

with open("input") as file:
    data = file.readlines()

data = [[line, 1] for line in data]

for i, line in enumerate(data):
    all_numbers = re.findall("\d+", line[0])
    matches = len(set(all_numbers[1:11]).intersection(set(all_numbers[11:])))
    for j in range(i + 1, i + matches + 1):
        data[j][1] += line[1]

print(sum([line[1] for line in data]))
