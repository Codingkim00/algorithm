# 괄호 문자열이 주어질 때
# 올바른 괄호이면 yes, 아님면 no를 출력하시오

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    open = 0
    close = 0
    gwal = list(input().strip())
    pre = ""

    is_gwal = True

    for j in range(len(gwal)):
        if gwal[j] == ")":
            close += 1
            if close > open:
                is_gwal = False
                break

        elif gwal[j] == "(":
                open += 1

    if is_gwal:
        if open == close:
            print("yes")
        else:
            print("no")