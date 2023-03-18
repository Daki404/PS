import sys

input = sys.stdin.readline


grow_day, lay_day, dead_day, N = map(int, input().split())

dp = [0] * (N + 1)
dp[0] = 1

survive_bug = 0
for i in range(grow_day, N + 1):
    survive_bug = (survive_bug + dp[i - grow_day] - dp[i - lay_day]) % 1000 
    dp[i] = survive_bug

result = 0
for i in range(max(0, N-dead_day + 1), N + 1):
    result = (result + dp[i]) % 1000

print(result)