import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

group = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            q = deque([(i, j)])
            map[i][j] = 0
            count = 1

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0<= nx < N and 0 <= ny < N:
                       if map[nx][ny] == 1:
                           map[nx][ny] = 0
                           q.append((nx,ny))
                           count += 1

            group.append(count)

print(len(group))
group.sort()
for i in range(len(group)):
    print(group[i])

