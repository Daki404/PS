import sys; input = sys.stdin.readline


n, m = map(int, input().split())
values = [[0] * (n+2)]

for _ in range(n):
    line = list(map(int, input().split()))
    values.append(line)


dp = [[0] * (n+2) for _ in range(m+2)]
path = [[0] * (n+2) for _ in range(m+2)]

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j]

        for k in range(1, j+1):
            if dp[i][j] < (tmp := values[k][i] + dp[i-1][j-k]):
                dp[i][j] = tmp
                path[i][j] = k

print(dp[m][n])
result = []
for i in range(m, 0, -1):
    picked = path[i][n] 
    result.append(picked)
    n -= picked

print(*result[::-1])