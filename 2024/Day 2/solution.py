import csv


with open("data.csv", newline="") as file:
    data = list(csv.reader(file, delimiter=" "))
    data = [[int(e) for e in lst] for lst in data]


def invalid(previous: int, current: int, increasing: bool) -> bool:
    if current == previous:
        return True
    elif abs(current - previous) > 3:
        return True
    elif increasing is True and previous > current:
        return True
    elif increasing is False and previous < current:
        return True
    else:
        return False


def is_safe(lst: list) -> bool:
    for i in range(len(lst)):
        current = lst[i]
        if i == 0:
            previous = current
            increasing = lst[0] < lst[1]
            continue

        if invalid(previous, current, increasing):
            return False

        previous = current

    return True


safe = [is_safe(level) for level in data]
print("Part 1:", sum(safe))


def is_safe2(level):
    if is_safe(level):
        return True
    for i in range(len(level)):
        array = level.copy()
        array.pop(i)
        if is_safe(array):
            return True
    return False


safe = [is_safe2(level) for level in data]
print("Part 2:", sum(safe))
