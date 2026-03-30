import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [False] * (N+1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")

    for next in graph[v]:
        if not visited_dfs[next]:
            dfs(next)


def bfs(v):
    visited_bfs = [False] * (N+1)
    q = deque([v])
    visited_bfs[v] = True

    while q:
        x = q.popleft()
        print(x, end=" ")

        for next in graph[x]:
            if not visited_bfs[next]:
                visited_bfs[next] = True
                q.append(next)

dfs(V)
print()
bfs(V)