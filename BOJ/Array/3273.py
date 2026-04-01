import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

count = 0

result = int(input())

left = 0
right = N - 1
nums.sort()

while left < right:
	sum = nums[left] + nums[right]

	if sum == result:
		count += 1
		left += 1
		right -= 1
	elif sum < result:
		left += 1
	else:
		right -= 1

print(count)