import re
from math import sqrt, ceil, floor

with open("input") as file:
    data = file.readlines()

result = [re.findall("\d+", line) for line in data]

race_data = []
for i in range(len(result[0])):
    race_data.append((int(result[0][i]), int(result[1][i])))

print(race_data)

result = None

for best_time, best_distance in race_data:
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

    if result == None:
        result = fastest - slowest + 1
    else:
        result = result * (fastest - slowest + 1)

print(result)
