import sys

input = sys.stdin.readline


n = int(input())

t = []
p = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a - 1)
    p.append(b)

for i in range(n - 1, -1 , -1):
    if i + t[i] >= n:
        p[i] = 0
    elif i + t[i] == n - 1:
        p[i] = p[i]
    else:
        p[i] += max(p[i + t[i] + 1:])

print(max(p))