n, m = map(int, input().split())
line = list(range(1, n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    line[a-1], line[b-1] = line[b-1], line[a-1]
print(*line)