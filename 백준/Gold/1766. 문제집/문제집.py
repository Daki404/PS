from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline


n, m = map(int, input().split())

line = [0] * (n + 1)
prior_grpah = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    prior_grpah[a].append(b)
    line[b] += 1

min_heap = []
for i in range(1, n + 1):
    if not line[i]:
        heapq.heappush(min_heap, i)

while min_heap:
    node = heapq.heappop(min_heap)
    print(node, end=" ")

    for i in prior_grpah[node]:
        line[i] -= 1
        if not line[i]:
            heapq.heappush(min_heap, i)
