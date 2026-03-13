import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

p = [0]*(N+1)
q = deque([1])

while q:
    pp = q.popleft()

    for c in graph[pp]:
        if p[c] == 0:
            p[c] = pp
            q.append(c)

for i in range(2, N+1):
    print(p[i])


