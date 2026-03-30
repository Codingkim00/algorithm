import sys
input = sys.stdin.readline

while True:
    try:
        line = input()
        if not line:
            break
        A, B = map(int, line.split())
        print(A+B)

    except ValueError:
        continue