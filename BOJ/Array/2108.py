import sys
input = sys.stdin.readline

N = int(input())
nums = []

for i in range(N):
	a = int(input())
	nums.append(a)

nums.sort()

count = [0] * 8001

for x in nums:
	count[x + 4000] += 1

maxn = max(count)

su = []

for i in range(8001):
	if count[i] == maxn:
		su.append(i - 4000)

if len(su) > 1:
	result = su[1]
else:
	result = su[0]

print(round(sum(nums)/N))
print(nums[N//2])
print(result)
print(max(nums) - min(nums))