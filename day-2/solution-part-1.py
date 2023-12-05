import re

with open("input") as file:
    data = file.readlines()

regex_filter = "\d+ \w+"

result = 0

for i, line in enumerate(data):
    possible = True
    regex_match = re.findall(regex_filter, line)
    for entry in regex_match:
        split_entry = entry.split()
        if split_entry[1] == "red" and int(split_entry[0]) > 12:
            possible = False
        if split_entry[1] == "green" and int(split_entry[0]) > 13:
            possible = False
        if split_entry[1] == "blue" and int(split_entry[0]) > 14:
            possible = False

    if possible:
        result += i + 1

print(result)
