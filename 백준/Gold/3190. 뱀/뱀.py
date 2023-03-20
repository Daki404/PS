from typing import List
import sys

input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

HEAD_DIRECT = "URDL"
APPLE = -1
BLANK = 0


def init_field(n: int, apples: List[int]) -> List[List[int]]:
    field = [[0] * n for _ in range(n)]
    field[0][0] = 1
    
    for apple in apples:
        r, c = apple
        field[r - 1][c - 1] = APPLE
    
    return field


def move_snake(snake_idx: int, head_x: int, head_y: int, tail_x: int, tail_y: int) -> bool:
    def find_next_tail(tail_x:int, tail_y:int) -> List[int]:
        for i in range(4):
            new_x = tail_x + dx[i]
            new_y = tail_y + dy[i]
            
            if not (0 <= new_x < n) or not (0 <= new_y < n):
                 continue
            
            if field[new_y][new_x] == field[tail_y][tail_x] + 1:
                return new_x, new_y

    if (direction := HEAD_DIRECT[direct_idx]) == 'U':
        if head_y-1 < 0 or (next_pos := field[head_y-1][head_x]) > BLANK:
            return False
        field[head_y-1][head_x] = snake_idx
        head_y -= 1
    
    elif direction == 'R':
        if head_x+1 >= n or (next_pos := field[head_y][head_x+1]) > BLANK:
                return False
        field[head_y][head_x+1] = snake_idx
        head_x += 1
    
    elif direction == 'D':
        if n <= head_y+1 or (next_pos := field[head_y+1][head_x]) > BLANK:
                return False
        field[head_y+1][head_x] = snake_idx
        head_y += 1

    else:
        if head_x-1 < 0 or (next_pos := field[head_y][head_x-1]) > BLANK:
                return False
        field[head_y][head_x-1] = snake_idx
        head_x -= 1

    grow = False

    if next_pos == APPLE:
            grow = True

    if not grow:
        x, y = tail_x, tail_y

        tail_x, tail_y = find_next_tail(tail_x, tail_y)
        field[y][x] = 0
    
    return head_x, head_y, tail_x, tail_y


if __name__ == '__main__':
    n = int(input())

    apple_num = int(input())
    apples = [list(map(int, input().split())) for _ in range(apple_num)]

    spin_num = int(input())
    spins = {}
    for _ in range(spin_num):
        time, direct = input().strip().split()
        spins[int(time) + 1] = direct

    field = init_field(n, apples)

    head_x = head_y = 0
    tail_x = tail_y = 0
    
    direct_idx = 1
    snake_idx = 1
    timer = 0

    while True:
        timer += 1
        snake_idx += 1

        if (tmp := spins.get(timer)) is not None:
            if tmp == 'L':
                direct_idx -= 1
                if direct_idx < 0: direct_idx = 3
            else:
                direct_idx = (direct_idx + 1) % 4

        result = move_snake(snake_idx, head_x, head_y, tail_x, tail_y)

        if isinstance(result, tuple):
            head_x, head_y, tail_x, tail_y = result
        else:
            print(timer)
            break