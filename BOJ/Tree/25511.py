import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(n-1):
    p,c = map(int, input().split())
    graph[p].append(c)

nodes = list(map(int, input().split()))
a = nodes.index(k)

depth = [0]*n

q = deque([0])

while q:
    pp = q.popleft()

    for cc in graph[pp]:
        depth[cc] = depth[pp] + 1
        q.append(cc)

print(depth[a])