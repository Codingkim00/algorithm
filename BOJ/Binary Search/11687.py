import sys
input = sys.stdin.readline

def zero(n: int) -> int:
    cnt = 0
    while n:
        n //= 5
        cnt += n
    return cnt

M = int(input().strip())

lo, hi = 0, 5 * M
ans = -1

while lo <= hi:
    mid = (lo + hi) // 2
    z = zero(mid)
    if z >= M:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans if ans != -1 and zero(ans) == M else -1)
