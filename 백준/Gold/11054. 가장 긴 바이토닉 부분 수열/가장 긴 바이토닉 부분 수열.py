import sys

input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
reverse_line = line[::-1]
dp_up = [1]
dp_down = [1]

for i in range(1, n):
    up_high = 0
    down_high = 0
    for j in range(i):
        if line[j] < line[i]:
            up_high = max(dp_up[j], up_high)
        if reverse_line[j] < reverse_line[i]:
            down_high = max(dp_down[j], down_high)
    
    dp_up.append(up_high + 1)
    dp_down.append(down_high + 1)


print(max([i + j for i, j in zip(dp_up, dp_down[::-1])]) - 1)