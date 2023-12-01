import re

with open("input") as file:
    data = file.readlines()

dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

regex_filter = f"(?=({'|'.join(list(dict.keys()))}))"

count = 0

for line in data:
    result = re.findall(regex_filter, line)

    count += 10 * dict[result[0]] + dict[result[-1]]

print(count)
