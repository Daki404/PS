import sys; input = sys.stdin.readline

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


def get_union() -> bool:
    def dfs(x: int, y:int) -> bool:
        stack = [(x, y)]
        area_cnt = 0
        people_cnt = 0
        area_idx = []

        while stack:
            x, y = stack.pop()
            
            if visited[y][x]:
                continue

            area_cnt += 1
            people_cnt += field[y][x]
            area_idx.append((y, x))
            visited[y][x] = True

            for dx, dy in zip(DX, DY):
                new_x = x + dx
                new_y = y + dy

                if not(0<=new_x<n)\
                        or not(0<=new_y<n)\
                        or visited[new_y][new_x]\
                        or abs(field[y][x] - field[new_y][new_x]) < l\
                        or abs(field[y][x] - field[new_y][new_x]) > r:
                    continue
                
                stack.append((new_x, new_y))

        for h, w in area_idx:
            field[h][w] = people_cnt // area_cnt

        return len(area_idx) > 1

    is_moved = False
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            is_moved = max(is_moved, dfs(i, j))
    
    return is_moved
    

n, l, r = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

day = 0
while get_union():
    day += 1

print(day)