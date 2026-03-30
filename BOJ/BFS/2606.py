import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
count = 0

#connected
con = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    con[a].append(b)
    con[b].append(a)

virus = [False] * (N+1)
q = deque([1])
virus[1] = True

while q:
    x = q.popleft()

    for next in con[x]:
        if not virus[next]:
            virus[next] = True
            q.append(next)
            count += 1

print(count)