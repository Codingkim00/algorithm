from collections import deque

N, M = map(int, input().split())
a = list(map(int, input().split()))

total = 0

q = deque()

for i in range(N):
    q.append(i+1)


for target in a :

    id = q.index(target)

    left = id
    right = len(q) - id

    if left <= right:
        q.rotate(-left)
        total += left

    else:
        q.rotate(right)
        total += right

    q.popleft()

print (total)

