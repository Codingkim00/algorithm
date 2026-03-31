import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dont = [[-1]*M for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            q.append((i,j))
            dont[i][j] = 0

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if maps[nx][ny] == 1 and dont[nx][ny] == -1:
                dont[nx][ny] = dont[x][y] + 1
                q.append((nx,ny))

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            print(maps[i][j], end=' ')
        else:
            print(dont[i][j], end=' ')
    print()