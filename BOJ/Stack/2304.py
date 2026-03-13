import sys

N = int(sys.stdin.readline().strip())

h = [0] * 1001
l = 1001
r = 0
maxh = 0
maxhl = 0

for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    h[L] = H
    if L < l:
        l = L
    if L > r:
        r = L
    if H > maxh:
        maxh = H
        maxhl = L

area = 0

S = 0
for x in range(l, maxhl + 1):
    if h[x] > S:
        S = h[x]
    area += S

S = 0
for x in range(r, maxhl, -1):
    if h[x] > S:
        S = h[x]
    area += S

print(area)
