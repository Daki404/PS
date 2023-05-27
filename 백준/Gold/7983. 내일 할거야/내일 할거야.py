import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.sort(key = lambda x: (x[1], x[0]))

for i in range(n - 1, 0, -1):
    now_d, now_t = data[i]
    prev_d, prev_t = data[i - 1]

    if  (now_time := now_t - now_d) < prev_t:
        data[i - 1][1] = now_time

print(data[0][1] - data[0][0])