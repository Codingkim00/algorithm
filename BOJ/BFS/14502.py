import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0

empty = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            empty.append((i, j))

def bfs():
    temp = [row[:] for row in maps]
    q = deque()

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))

    zero = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                zero += 1
    return zero

def dfs(cnt, start):
    global count

    if cnt == 3:
        count = max(bfs(),count)
        return

    for a in range(start, len(empty)):
        x, y = empty[a]
        maps[x][y] = 1
        dfs(cnt + 1, a + 1)
        maps[x][y] = 0


dfs(0,0)
print(count)