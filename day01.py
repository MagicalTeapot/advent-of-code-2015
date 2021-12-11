from collections import Counter
with open("day01_input.txt") as f:
    data = f.read().strip()
counts = Counter(data)
print("Part 1:", counts["("] - counts[")"])

floor = 0
for pos, bracket in enumerate(data, 1):
    floor += 1 if bracket == "(" else -1
    if floor < 0:
        break
print("Part 2:", pos)