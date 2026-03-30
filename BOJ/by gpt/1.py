# 숫자 뒤집기
# 입력된 정수를 뒤집어서 출력하시오

import sys
input = sys.stdin.readline

N = list(input().strip())

N.reverse()

N = "".join(N)

print(N)


