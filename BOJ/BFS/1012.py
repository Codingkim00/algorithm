import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    M, N, K = map(int, input().split())
    # gw = gangwondo
    gw = [[0] * M for _ in range(N)]
    group = 0

    for i in range(K):
        a, b = map(int, input().split())
        gw[b][a] = 1

    for i in range(N):
        for j in range(M):
            if gw[i][j] == 1:
                q = deque([(i, j)])
                gw[i][j] = 0

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < N and 0 <= ny < M:
                            if gw[nx][ny] == 1:
                                gw[nx][ny] = 0
                                q.append((nx, ny))

                group += 1

    print(group)