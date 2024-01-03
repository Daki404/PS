import sys; input = sys.stdin.readline
from collections import deque


DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]


def get_score(x: int, y: int) -> int:
    if score_field[y][x]:
        return score_field[y][x]
    
    visited = set([(x, y)])
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()

        for dx, dy in zip(DX, DY):
            new_x = x + dx
            new_y = y + dy

            if not(0<=new_x<w)\
                    or not(0<=new_y<h)\
                    or field[new_y][new_x] != field[y][x]\
                    or (new_x, new_y) in stack\
                    or (new_x, new_y) in visited:
                continue

            visited.add((new_x, new_y))
            stack.append((new_x, new_y))
    
    score = field[y][x] * len(visited)
    for x, y in visited:
        score_field[y][x] = score
    
    return score


dice_row = deque([4, 6, 3])
dice_col = deque([2, 6, 5])
direction = 0

h, w, k = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(h)]
score_field = [[0] * w for _ in range(h)]

dice_x = dice_y = 0
total_score = 0 
for _ in range(k):
    if not(0<=dice_x+DX[direction]<w)\
            or not(0<=dice_y+DY[direction]<h):
        direction = (direction + 2)%len(DX)
    
    dice_x += DX[direction]
    dice_y += DY[direction]

    if direction == 0:
        dice_row.append(7 - dice_row[1])
        dice_row.popleft()
        dice_col[1] = dice_row[1]
    elif direction == 1:
        dice_col.append(7 - dice_col[1])
        dice_col.popleft()
        dice_row[1] = dice_col[1]
    elif direction == 2:
        dice_row.appendleft(7 - dice_row[1])
        dice_row.pop()
        dice_col[1] = dice_row[1]
    else:
        dice_col.appendleft(7 - dice_col[1])
        dice_col.pop()
        dice_row[1] = dice_col[1]

    if dice_col[1] > (now_num := field[dice_y][dice_x]):
        direction = (direction+1)%4
    elif dice_col[1] < now_num:
        direction = (direction+3)%4

    total_score += get_score(dice_x, dice_y)

  
print(total_score)