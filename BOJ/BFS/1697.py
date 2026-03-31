import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

line = [0] * 100001
line[N] = 1


q = deque()
q.append(N)

while q:
    x = q.popleft()

    if x == M:
        print(line[x]-1)
        break

    for nx in (x+1,x-1,x*2):
        if 0 <= nx < 100001 and line[nx] == 0:
            line[nx] = line[x] + 1
            q.append(nx)