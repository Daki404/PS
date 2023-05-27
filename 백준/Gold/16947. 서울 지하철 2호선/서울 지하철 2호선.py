import sys

input = sys.stdin.readline


def dfs(field):
    for st in range(1, n + 1):
        log = []
        out_log = []
        visited = set([st])
        stack = [(st, [st])]

        while stack:
            node, path = stack.pop()
            visited.add(node)

            for i in field[node]:
                if i in visited:
                    if i == st and len(path) != 2:
                        log += path
                    else:
                        out_log.append(path)
                    continue

                stack.append((i, path[:] + [i]))
        if set(log):
            return set(log), out_log


    

n = int(input())
field = {i:[] for i in range(1, n+1)}

for _ in range(n):
    a, b = map(int, input().split())
    field[a].append(b)
    field[b].append(a)

cross_node, out_node = dfs(field)
result = [0] * (n+1)

for i in out_node:
    if (st := i[-1]) in cross_node:
        continue
    
    for j in range(len(i)-1, -1, -1):
        if i[j] in cross_node:
            result[st] = len(i)-j-1
            break

print(*result[1:])