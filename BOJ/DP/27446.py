import sys
input = sys.stdin.readline

N, M = map(int, input().split())
page = set(map(int, input().split()))

dp = [float("inf")] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    if i in page:
        dp[i] = dp[i-1]

    for j in range(1, i+1):
        ink = 5 + 2*(i - j + 1)
        dp[i] = min(dp[i], dp[j-1] + ink)

print(dp[N])