import sys; input = sys.stdin.readline

x, y, w, s = map(int, input().split())
mininum_time = 0
min_distance = min(w, s)


if 2*w > s:
    min_len = min(x, y)
    mininum_time += s * min_len
    x -= min_len
    y -= min_len

for _ in range(x//2):
    mininum_time += 2*min_distance
mininum_time += (x%2) * w

for _ in range(y//2):
    mininum_time += 2*min_distance
mininum_time += (y%2) * w

print(mininum_time)