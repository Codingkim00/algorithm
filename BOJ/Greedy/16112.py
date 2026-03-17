import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
exp = 0

a.sort(reverse=True)

for i in range(k):
    exp += a[i] * (n - k + 1)

