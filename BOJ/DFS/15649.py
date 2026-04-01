import sys
input = sys.stdin.readline

N, M = map(int, input().split())

su = []
visited = [False] * (N + 1)

def dfs():
    if len(su) == M:
        print(*su)

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            su.append(i)

            dfs()

            su.pop()
            visited[i] = False

dfs()