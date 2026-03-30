# 미로에서 벽을 딱 1번 부술 수 있다
# 최단거리 구하기

import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

while q:
    x, y, wall = q.popleft()

    if x == N-1 and y == M-1:
        print(visited[x][y][wall])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:

           if miro[nx][ny] == 0 and visited[nx][ny][wall] == 0:
               visited[nx][ny][wall] = visited[x][y][wall] + 1
               q.append((nx, ny, wall))

           if miro[nx][ny] == 1 and wall == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))