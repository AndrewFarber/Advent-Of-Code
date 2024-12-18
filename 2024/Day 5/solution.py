import csv
from math import floor
from collections import defaultdict


left_rules = defaultdict(list)
right_rules = defaultdict(list)

type_ = "data"
with open(f"{type_}_rules.txt") as file:
    data = list(csv.reader(file, delimiter="|"))
    for left, right in data:
        left_rules[int(right)].append(int(left))
        right_rules[int(left)].append(int(right))

with open(f"{type_}_pages.txt") as file:
    pages = list(csv.reader(file, delimiter=","))
    pages = [[int(i) for i in pg] for pg in pages]

invalid_orders = []


def score(pages: list[int]) -> int:
    for i in range(len(pages) - 1):
        left = pages[i]
        right = pages[i + 1 :]
        for ele in right:
            valid_values = left_rules.get(ele, None)
            invalid_values = right_rules.get(ele, None)
            if valid_values is not None and left not in valid_values:
                invalid_orders.append(pages)
                return 0
            if invalid_values is not None and left in invalid_values:
                invalid_orders.append(pages)
                return 0
    return pages[floor(len(pages) / 2.0)]


scores = []
for pgs in pages:
    scores.append(score(pgs))

print("Part 1:", sum(scores))


def reorder(pages: list[int]) -> list[int]:
    for i in range(len(pages) - 1):
        left = pages[i]
        right = pages[i + 1]
        left_values = left_rules.get(right, None)
        right_values = right_rules.get(left, None)
        if left_values is not None and left not in left_values:
            pages[i] = right
            pages[i + 1] = left
            return reorder(pages)
        if right_values is not None and right not in right_values:
            pages[i] = right
            pages[i + 1] = left
            return reorder(pages)
    return pages


scores = []
for lst in invalid_orders:
    scores.append(score(reorder(lst)))

print("Part 2:", sum(scores))
