import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

maxnum = max(numbers)
minnum = min(numbers)

print(minnum, maxnum)