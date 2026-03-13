import sys
input  = sys.stdin.readline

S = input().strip()
sorted_S = sorted(S)
result = []
n = len(S)

def is_anti(S):
    n = len(S)
    for i in range(n//2):
        if S[i] == S[n-i-1]:
            return False
    return True

if is_anti(sorted_S):
    print(''.join(sorted_S))
else:
    mid = n // 2
    left = sorted_S[:mid]
    right = sorted_S[mid:]
    result = [''] * n

    for i in range(mid):
        result[i] = left[i]
        result[n-1-i] = right[(n//2)-i-1]

    if n % 2:
        result[mid] = right[-1]

    print(''.join(result))
