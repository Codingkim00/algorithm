import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
output = []
num = list(range(1,N))
num.sort(reverse=True)

num = deque(num)

if N % 4 == 2 or N % 4 == 3:
    print(N-1)
    while len(num) > 1:
        x = num.popleft()
        y = num.popleft()
        output.append((x, y))
        num.append(abs(x - y))

    if len(num) == 1:
        output.append((num[0], N))

    for x, y in output:
        print(x, y)

else:
    print(N)
    while len(num) > 1:
        x = num.popleft()
        y = num.popleft()
        output.append((x, y))
        num.append(abs(x - y))

    if len(num) == 1:
        output.append((num[0], N))

    for x, y in output:
        print(x, y)



