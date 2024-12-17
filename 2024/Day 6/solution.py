with open("data.txt") as file:
    raw = file.read().strip()
    G = raw.split("\n")

R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == "^":
            sr, sc = r, c

p1 = 0
p2 = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

r, c = sr, sc
d = 0  # up=0, right=1, down=2, left=3
SEEN_RC = set()
while True:
    SEEN_RC.add((r, c))
    dr, dc = directions[d]
    rr = r + dr
    cc = c + dc
    # If outside of grid, then p1 ends
    if not (0 <= rr < R and 0 <= cc < C):
        break
    if G[rr][cc] == "#":
        d = (d + 1) % 4
    else:
        r = rr
        c = cc
print("P1:", len(SEEN_RC))

# Try every open square for obstacle
for o_r in range(R):
    for o_c in range(C):
        r, c = sr, sc
        d = 0  # up=0, right=1, down=2, left=3
        SEEN = set()
        while True:
            # Obstacle creates loop
            if (r, c, d) in SEEN:
                p2 += 1
                break
            SEEN.add((r, c, d))
            dr, dc = directions[d]
            rr = r + dr
            cc = c + dc
            # If outside of grid break
            if not (0 <= rr < R and 0 <= cc < C):
                break
            # If hit obstacle, change direction
            if G[rr][cc] == "#" or (rr == o_r and cc == o_c):
                d = (d + 1) % 4
            else:
                r = rr
                c = cc

print("P2:", p2)
