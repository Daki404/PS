import sys; input = sys.stdin.readline
from typing import List


DX = [-1, 0, 1, 0]
DY = [0, 1, 0, -1]

direction_to_idx = {
    1: 7,
    2: 3,
    3: 1,
    4: 5,
}


def init_bead(field: List[List[int]]) -> List[int]:
    x = y = field_size//2
    direction = 0
    bead_stack = [field[y][x]]

    for i in range(1, field_size):
        for _ in range(2):
            for _ in range(i):
                x += DX[direction]
                y += DY[direction]
                
                if field[y][x] == 0:
                    return bead_stack
                
                bead_stack.append(field[y][x])
            
            direction = (direction+1) % 4

    for _ in range(field_size - 1):
        x += DX[direction]
        y += DY[direction]
        if field[y][x] == 0:
            return bead_stack
        bead_stack.append(field[y][x])
    return bead_stack


def blizard(direction: int, size: int) -> None:
    idx = direction_to_idx[direction]
    weight = idx + 8
    remove_idx = []

    for _ in range(size):
        remove_idx.append(idx)
        idx += weight
        weight += 8
    
    for i in remove_idx[::-1]:
        if i < len(bead_stack):
            del bead_stack[i]


def explode_bead(bead_stack: List[int]) -> List[int]:
    if len(bead_stack) == 1:
        return [0], 0
    
    score = 0
    flag = True
    
    while flag\
            and len(bead_stack) >= 2:
        flag = False
        num = bead_stack[1]
        cnt = 0
        new_bead = [0]
        for bead in bead_stack[1:] + [-1]:
            if num == bead:
                cnt += 1
            else:
                if cnt >= 4:
                    score += num * cnt
                    del new_bead[-cnt:]
                    flag = True
                num = bead
                cnt = 1
            new_bead.append(bead)
        bead_stack = new_bead[:-1]

    return bead_stack, score


def rearrange_bead(bead_stack: List[int]) -> List[int]:
    if len(bead_stack) == 1:
        return [0]
    
    num = bead_stack[1]
    cnt = 0
    new_bead = [0]
    
    for bead in bead_stack[1:]+[-1]:
        if num != bead:
            new_bead.append(cnt)
            new_bead.append(num)
            num = bead
            cnt = 0
        cnt += 1
    
    return new_bead[:field_size*field_size-1]


field_size, cmd_cnt = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(field_size)]

score = 0
bead_stack = init_bead(field)

for _ in range(cmd_cnt):    
    direction, size = map(int, input().split())
    blizard(direction, size)

    exploded_bead, tmp_score = explode_bead(bead_stack)
    score += tmp_score

    bead_stack = rearrange_bead(exploded_bead)
print(score)