from collections import defaultdict
from itertools import combinations

with open("data.txt") as file:
    raw = file.readlines()
    G = [r.rstrip("\n") for r in raw]

R: int = len(G)
C: int = len(G[0])
CHARS: dict[str, list[tuple[int, int]]] = defaultdict(list)
SOLUTIONS_P1: set = set()
SOLUTIONS_P2: set = set()


class Antinodes:
    def __init__(self, p1: tuple[int, int], p2: tuple[int, int]):
        self.p1 = p1
        self.p2 = p2
        self.slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        self.intercept = p1[1] - self.slope * p1[0]
        self.x_distance = p2[0] - p1[0]
        self.y_distance = p2[1] - p1[1]

    def get_p1(self):
        results = []

        if (0 <= self.p1[0] - self.x_distance < R) and (
            0 <= self.p1[1] - self.y_distance < C
        ):
            results.append((self.p1[0] - self.x_distance, self.p1[1] - self.y_distance))

        if (0 <= self.p2[0] + self.x_distance < R) and (
            0 <= self.p2[1] + self.y_distance < C
        ):
            results.append((self.p2[0] + self.x_distance, self.p2[1] + self.y_distance))
        return results

    def get_p2(self):
        results = []
        for i in range(-1000, 1000):
            x = self.p1[0] - i * self.x_distance
            y = self.p1[1] - i * self.y_distance
            if x == int(x) and y == int(y):
                if (0 <= x < R) and (0 <= y < C):
                    results.append((x, y))
        return results


for i in range(R):
    for j in range(C):
        char = G[i][j]
        if char != ".":
            CHARS[char].append((i, j))


for char, lst in CHARS.items():
    for r in combinations(lst, 2):
        a = Antinodes(r[0], r[1])
        for x in a.get_p1():
            SOLUTIONS_P1.add(x)
        for x in a.get_p2():
            SOLUTIONS_P2.add(x)

print("P1:", len(SOLUTIONS_P1))
print("P2:", len(SOLUTIONS_P2))
