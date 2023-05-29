from collections import deque
import sys

input = sys.stdin.readline


def find_cycle_node(field, st=1):
    log = []
    stack = [(st, [st])]

    while stack:
        node, path = stack.pop()

        for i in field[node]:
            if i in path:
                if path[-2] != i:
                    return path[(path.index(i)):]
                continue
            stack.append((i, path[:] + [i]))


def get_bfs_distance(field, cross_node):
    visit = set([cross_node[0]])
    queue = deque([(cross_node[0], 0)])
    result = [0] * (len(field)+1)

    while queue:
        node, cost = queue.popleft()
        result[node] = cost
        
        for i in field[node]:
            if i in visit:
                continue
            if i in cross_node:
                queue.append((i, 0))
            else:
                queue.append((i, cost + 1))
            visit.add(i)
    return result[1:]


n = int(input())
field = {i:[] for i in range(1, n+1)}

for _ in range(n):
    a, b = map(int, input().split())
    field[a].append(b)
    field[b].append(a)

cross_node = find_cycle_node(field)
result = get_bfs_distance(field, cross_node)

print(*result)