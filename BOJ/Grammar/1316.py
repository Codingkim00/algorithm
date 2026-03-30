import sys
input = sys.stdin.readline

N = int(input())
group = 0

for i in range(N):
    char = list(input().strip())
    word = set()
    pre = ""

    is_group = True

    for x in char:
        if x != pre:
            if x in word:
                is_group = False
                break
            pre = x
            word.add(x)

    if is_group:
        group += 1

print(group)
