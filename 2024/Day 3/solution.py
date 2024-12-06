import re


with open("data.txt") as file:
    data = file.read()

pattern = r"(\bdo\b)|(don't)|mul\((\d{1,3},\d{1,3})\)"
prog = re.compile(pattern)

x = prog.findall(data)
x = [i[0] or i[1] or i[2] for i in x]
print(x)

on = True
numbers = []
for nums in x:
    if nums == "do":
        on = True
    elif nums == "don't":
        on = False
    else:
        if on:
            x, y = nums.split(",")
            numbers.append(int(x) * int(y))

print("Part 2:", sum(numbers))
