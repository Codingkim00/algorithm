import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    stack = input().split()

    if stack[0] == 'push':
        q.append(stack[1])

    elif stack[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.pop())

    elif stack[0] == 'size':
        print(len(q))

    elif stack[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif stack[0] == 'top':
        if not q:
            print(-1)
        else:
            print(q[-1])