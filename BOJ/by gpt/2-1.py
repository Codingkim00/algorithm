# 괄호 문자열이 주어질 때
# 올바른 괄호이면 yes, 아님면 no를 출력하시오

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    stack = []
    gwal = input().strip()

    for x in gwal:
        if x == "(":
            stack.append(x)

        else:
            if not stack:
                print("no")
                break
            stack.pop()

    else:
        if not stack:
            print("yes")
        else:
            print("no")