# N x M 미로가 주어진다.
# 1은 이동가능, 0은 벽이다
# (1,1) -> (N,M)까지 최소 이동 횟수 출력

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
miro = [list(map(int,input().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                q.append((nx, ny))


print(miro[N-1][M-1])


