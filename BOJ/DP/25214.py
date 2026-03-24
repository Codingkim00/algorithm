import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
result = deque()

maxnum = 0
minnum = num[0]

for x in num:
    maxnum = max(maxnum, x - minnum)
    minnum = min(minnum, x)
    result.append(maxnum)

print(*result)