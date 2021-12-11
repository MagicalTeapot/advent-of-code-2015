from itertools import combinations
from math import prod
def loop_input():
    with open("day02_input.txt") as f:
        for line in f:
            yield [int(n) for n in line.strip().split("x")]

answer = 0
for dimensions in loop_input():
    side_areas = [x * y for x, y in combinations(dimensions, 2)]
    answer += sum(2 * area for area in side_areas) + min(side_areas)
print("Part 1:", answer)

answer = 0
for dimensions in loop_input():
    answer += 2 * (sum(dimensions) - max(dimensions)) + prod(dimensions)
print("Part 2", answer)