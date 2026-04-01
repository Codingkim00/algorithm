import sys
input = sys.stdin.readline

nums = []

for i in range(9):
	N = int(input())
	nums.append(N)

mx = max(nums)
idmx = nums.index(mx)

print(mx)
print(idmx)