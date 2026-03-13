import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()

for _ in range(M):
    start, end = map(int, input().split())

    left, right = 0, N
    while left < right:
        mid = (left + right) // 2
        if dot[mid] >= start:
            right = mid
        else:
            left = mid + 1
    lb = left

    left, right = 0, N
    while left < right:
        mid = (left + right) // 2
        if dot[mid] > end:
            right = mid
        else:
            left = mid + 1
    ub = right

    print(ub - lb)

