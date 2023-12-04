import re

with open("input") as file:
    data = file.readlines()

print(
    sum(
        [
            2
            ** (
                len(
                    set(re.findall("\d+", line)[1:11]).intersection(
                        set(re.findall("\d+", line)[11:])
                    )
                )
                - 1
            )
            for line in data
            if len(
                set(re.findall("\d+", line)[1:11]).intersection(
                    set(re.findall("\d+", line)[11:])
                )
            )
            > 0
        ]
    )
)
