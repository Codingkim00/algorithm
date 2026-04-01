import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
su = []
arr.sort()

visited = [False] * (N+1)

def dfs():

    if len(su) == M:
        print(*su)
        return

    for i in range(N):
        if not visited[i]:
            su.append(arr[i])
            visited[i] = True
            dfs()
            su.pop()
            visited[i] = False

dfs()

