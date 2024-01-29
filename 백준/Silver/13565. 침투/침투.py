import sys; input = sys.stdin.readline
from typing import List

DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]


def dfs(st_nodes: List[int]) -> bool:
    stack = []

    for pos in st_nodes:
        x, y = pos
        field[y][x] = 1
        stack.append(pos)

    while stack:
        x, y = stack.pop()
        if y == h-1:
            return True

        for dx, dy in zip(DX, DY):
            new_x = x + dx
            new_y = y + dy

            if not(0<=new_x<w)\
                    or not(0<=new_y<h)\
                    or field[new_y][new_x]:
                continue

            stack.append((new_x, new_y))
            field[new_y][new_x] = 1

    return False



h, w = map(int, input().split())
field = [list(map(int, input().strip())) for _ in range(h)]

st_nodes = []
for i in range(w):
    if field[0][i]:
        continue

    st_nodes.append((i, 0))

ret = dfs(st_nodes)
print("YES" if ret else "NO")