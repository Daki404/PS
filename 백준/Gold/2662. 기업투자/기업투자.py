import sys; input = sys.stdin.readline


n, m = map(int, input().split())
values = [[0] * (n+2)]

for _ in range(n):
    line = list(map(int, input().split()))
    values.append(line)


dp = [[0] * (n+2) for _ in range(m+2)]

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j]
        for k in range(1, j+1):
            dp[i][j] = max(dp[i][j], values[k][i] + dp[i-1][j-k])

print(dp[m][n])

idx = m
cost = n
result = []
while idx > 0:
    for i in range(cost+1):
        if (values[i][idx] + dp[idx-1][cost-i]) == dp[idx][cost]:
            result.append(i)
            cost -= i
            break
    idx -= 1
    
print(*result[::-1])