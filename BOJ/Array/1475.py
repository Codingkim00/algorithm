import sys

input = sys.stdin.readline

N = list(map(int, input().strip()))

nums = [0] * 10

for i in range(len(N)):
    for j in range(10):
        if N[i] == j:
            nums[j] += 1

while True:
    if abs(nums[6] - nums[9]) == 1 or nums[6] == nums[9]:
        break

    if nums[6] >= nums[9]:
        nums[9] += 1
        nums[6] -= 1
    elif nums[9] > nums[6]:
        nums[6] += 1
        nums[9] -= 1

print(max(nums))

