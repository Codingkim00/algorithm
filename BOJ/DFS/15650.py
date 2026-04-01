import sys
input = sys.stdin.readline

N, M = map(int, input().split())

su = []

def dfs(start):

    if len(su) == M:
        print(*su)
        return

    for i in range(start,N+1):
        su.append(i)
        dfs(i + 1)
        su.pop()

dfs(1)