with open("data.txt") as file:
    raw = file.readlines()
    data = [r.split(": ") for r in raw]
    data = [
        (int(row[0]), list(map(int, row[1].rstrip("\n").split(" ")))) for row in data
    ]


def valid_1(answer, nums):
    if len(nums) == 1:
        return nums[0] == answer
    if valid_1(answer, [nums[0] + nums[1]] + nums[2:]):
        return True
    if valid_1(answer, [nums[0] * nums[1]] + nums[2:]):
        return True
    return False


def valid_2(answer, nums):
    if len(nums) == 1:
        return nums[0] == answer
    if valid_2(answer, [nums[0] + nums[1]] + nums[2:]):
        return True
    if valid_2(answer, [nums[0] * nums[1]] + nums[2:]):
        return True
    if valid_2(answer, [int(str(nums[0]) + str(nums[1]))] + nums[2:]):
        return True
    return False


tot_p1 = []
tot_p2 = []
for ans, nums in data:
    if valid_1(ans, nums):
        tot_p1.append(ans)
    if valid_2(ans, nums):
        tot_p2.append(ans)

print("P1:", sum(tot_p1))
print("P2:", sum(tot_p2))
