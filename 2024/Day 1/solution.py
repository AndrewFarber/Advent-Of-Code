import csv

lst1 = []
lst2 = []

# Populate lst1 and lst2
with open("data.csv") as file:
    data = csv.reader(file, delimiter=" ")

    for line in data:
        if line:
            lst1.append(int(line[0]))
            lst2.append(int(line[3]))


# Distance Score
scores = []
lst1_sorted = sorted(lst1)
lst2_sorted = sorted(lst2)

for i in range(len(lst1)):
    scores.append(abs(lst1_sorted[i] - lst2_sorted[i]))

print("Distance:", sum(scores))


# Similarity Score
def count(value):
    cnt = 0
    for element in lst2:
        if value == element:
            cnt += 1
    return cnt


scores = []

for element in lst1:
    scores.append(element * count(element))

print("Similarity:", sum(scores))
