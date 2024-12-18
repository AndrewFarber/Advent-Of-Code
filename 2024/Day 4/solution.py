with open("data.txt") as file:
    lines = file.readlines()
    raw = [row.rstrip("\n") for row in lines]

n_columns = len(raw[0])
n_rows = len(raw)

data = (
    ["~" * (n_columns + 8) for _ in range(4)]
    + ["~~~~" + row + "~~~~" for row in raw]
    + ["~" * (n_columns + 8) for _ in range(4)]
)

for row in data:
    print(row)

cnt = 0
for row in range(n_rows):
    for col in range(n_columns):
        i = row + 4
        j = col + 4

        n = data[i - 3][j] + data[i - 2][j] + data[i - 1][j] + data[i][j]
        nw = data[i - 3][j - 3] + data[i - 2][j - 2] + data[i - 1][j - 1] + data[i][j]
        ne = data[i - 3][j + 3] + data[i - 2][j + 2] + data[i - 1][j + 1] + data[i][j]

        e = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i][j + 3]
        w = data[i][j - 3] + data[i][j - 2] + data[i][j - 1] + data[i][j]

        s = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j]
        sw = data[i][j] + data[i + 1][j - 1] + data[i + 2][j - 2] + data[i + 3][j - 3]
        se = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3]

        if n in ("XMAS", "SAMX"):
            cnt += 1
        if nw in ("XMAS", "SAMX"):
            cnt += 1
        if ne in ("XMAS", "SAMX"):
            cnt += 1
        if e in ("XMAS", "SAMX"):
            cnt += 1
        if w in ("XMAS", "SAMX"):
            cnt += 1
        if s in ("XMAS", "SAMX"):
            cnt += 1
        if sw in ("XMAS", "SAMX"):
            cnt += 1
        if se in ("XMAS", "SAMX"):
            cnt += 1

print("Probolem 1:", cnt / 2)

cnt = 0
for row in range(n_rows):
    for col in range(n_columns):
        i = row + 4
        j = col + 4

        nw = data[i - 1][j - 1] + data[i][j] + data[i + 1][j + 1]
        ne = data[i - 1][j + 1] + data[i][j] + data[i + 1][j - 1]
        if nw in ("MAS", "SAM") and ne in ("MAS", "SAM"):
            cnt += 1


print("Probolem 2:", cnt)
