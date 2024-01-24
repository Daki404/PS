import sys; input = sys.stdin.readline

DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]

def get_areas():
    def count_block(x: int, y: int) -> int:
        size = 0
        stack = [(x, y)]
        field[y][x] = True
    
        # dfs
        while stack:
            x, y = stack.pop()
            size += 1

            for dx, dy in zip(DX, DY):
                new_x = x + dx
                new_y = y + dy

                if not (0 <= new_x < w)\
                        or not (0 <= new_y < h)\
                        or field[new_y][new_x]:
                    continue
                
                field[new_y][new_x] = True
                stack.append((new_x, new_y))
        return size

    res = []
    for i in range(h):
        for j in range(w):
            if field[i][j]:
                continue

            res.append(count_block(j, i))
    
    return sorted(res)
    

h, w, c = map(int, input().split())
field = [[False] * w for _ in range(h)]

for _ in range(c):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            field[y][x] = True

res = get_areas()
print(len(res))
print(*res)