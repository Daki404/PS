from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
sorted_line = sorted(line)

idx_mapper = defaultdict(deque)
for i, j in enumerate(sorted_line):
    idx_mapper[j].append(i)

result = []
for i in line:
    result.append(idx_mapper[i].popleft())

print(*result)