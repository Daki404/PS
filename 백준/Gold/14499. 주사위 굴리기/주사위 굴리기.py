import sys
from typing import Tuple

input = sys.stdin.readline


dice_bot_eyes = 1
dice_stat = {'E':3, 'W':4, 'S':5, 'N':2}
eye_mapper = {i:0 for i in range(1, 7)}

n, m, y, x, k = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))


def get_direct(n: int) -> str:
    return "EWNS"[n - 1]


def move(direct: str) -> Tuple[int, int]:
    if direct == 'E':
        return 1, 0
    elif direct == 'W':
        return -1, 0
    elif direct == 'N':
        return 0, -1
    else:
        return 0, 1


def update_eyes(direct: str, bot_eyes: int, status: dict) -> Tuple[int, dict]:
    new_bot_eyes = status[direct]

    if direct == 'E':
        status['W'] = bot_eyes
        status['E'] = 7 - bot_eyes
    
    elif direct == 'W':
        status['E'] = bot_eyes
        status['W'] = 7 - bot_eyes
    
    elif direct == 'N':
        status['S'] = bot_eyes
        status['N'] = 7 - bot_eyes
    
    else:
        status['N'] = bot_eyes
        status['S'] = 7 - bot_eyes
    
    return new_bot_eyes, status 

for order in orders:
    direction = get_direct(order)

    new_x, new_y = move(direction)
    new_x += x
    new_y += y

    if not (0 <= new_x < m) \
            or not (0 <= new_y < n):
        continue

    x, y = new_x, new_y
    dice_bot_eyes, dice_stat = update_eyes(direction, dice_bot_eyes, dice_stat)

    if field_value := field[new_y][new_x]:
        eye_mapper[dice_bot_eyes] = field_value
        field[new_y][new_x] = 0
    
    else:
        field[new_y][new_x] = eye_mapper[dice_bot_eyes]
    
    print(eye_mapper[7 - dice_bot_eyes])