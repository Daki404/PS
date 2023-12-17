import sys
from typing import Tuple

sys.setrecursionlimit(10**6)

U, R, D, L = 0, 1, 2, 3
WALL, DIRTY, CLEAN = 1, 0, 2
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

input = sys.stdin.readline


def search_dirty(x: int, y: int) -> bool:
    for new_x, new_y in zip(dx, dy):
        new_x += x
        new_y += y

        if not(0 <= new_x < w) \
                or not(0 <= new_y < h):
            continue

        if field[new_y][new_x] == DIRTY:
            return True
    return False


def can_back(x: int, y: int, d:int) -> bool:
    if d == U:
        y += 1
    elif d == R:
        x -= 1
    elif d == D:
        y -= 1
    else:   #L
        x += 1

    if not(0 <= x < w) \
                or not(0 <= y < h)\
                or field[y][x] == WALL:
        return None
    return x, y

def can_go(x: int, y: int, d:int) -> Tuple[int]:
    if d == U:
        y -= 1
    elif d == R:
        x += 1
    elif d == D:
        y += 1
    else:   #L
        x -= 1

    if not(0 <= x < w) \
                or not(0 <= y < h)\
                or field[y][x] != DIRTY:
        return None
    return x, y

def change_direction(x: int, y: int, d:int) -> Tuple[int]:
    d -= 1
    if d < 0:
        d = 3
    
    if (new_pos := can_go(x, y, d)) is not None:
        x, y = new_pos
    
    return x, y, d


def clean(x: int, y: int, d:int) -> int:
    if field[y][x] == DIRTY:
        field[y][x] = CLEAN
        return 1 + clean(x, y, d)
    
    is_near_dirty = search_dirty(x, y)

    if is_near_dirty:
        new_x, new_y, new_d = change_direction(x, y, d)
        return clean(new_x, new_y, new_d)
    
    else:
        if (new_pos := can_back(x, y, d)) is not None:
            new_x, new_y = new_pos
            return clean(new_x, new_y, d)
        
        else:
            return 0
        


h, w = map(int, input().split())
r, c, d = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(h)]

print(clean(c, r, d))