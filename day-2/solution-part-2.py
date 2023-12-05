import re

with open("input") as file:
    data = file.readlines()

regex_filter = "\d+ \w+"

result = 0

for line in data:
    regex_match = re.findall(regex_filter, line)
    minimum_red = 0
    minimum_green = 0
    minimum_blue = 0

    for entry in regex_match:
        split_entry = entry.split()
        if split_entry[1] == "red":
            minimum_red = max([minimum_red, int(split_entry[0])])
        if split_entry[1] == "green":
            minimum_green = max([minimum_green, int(split_entry[0])])
        if split_entry[1] == "blue":
            minimum_blue = max([minimum_blue, int(split_entry[0])])

    result += minimum_red * minimum_green * minimum_blue

print(result)
