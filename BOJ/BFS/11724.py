import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
line = [[] for _ in range(N+1)]

group = 0
team = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    line[u].append(v)
    line[v].append(u)

def bfs(start):
    q = deque([start])
    team[start] = True

    while q:
        x = q.popleft()

        for nxt in line[x]:
            if not team[nxt]:
                team[nxt] = True
                q.append(nxt)


for i in range(1, N+1):
    if not team[i]:
        bfs(i)
        group += 1


print(group)



