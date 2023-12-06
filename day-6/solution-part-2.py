import re
from math import sqrt, ceil, floor

# I know this is ugly and doesn't account for edge cases but I only needed it to work in one case

with open("input") as file:
    data = file.readlines()

result = [re.findall("\d+", line) for line in data]

print(result)

best_time = int("".join(result[0]))
best_distance = int("".join(result[1]))

print(best_time)
print(best_distance)

slowest = (best_time - sqrt(best_time**2 - 4 * best_distance)) / 2.0
fastest = (best_time + sqrt(best_time**2 - 4 * best_distance)) / 2.0

if ceil(slowest) == slowest:
    slowest += 1
else:
    slowest = ceil(slowest)

if floor(fastest) == fastest:
    fastest -= 1
else:
    fastest = floor(fastest)

print((best_time - slowest) * slowest)
print((best_time - fastest) * fastest)

print(fastest)
print(slowest)

print(fastest - slowest + 1)
