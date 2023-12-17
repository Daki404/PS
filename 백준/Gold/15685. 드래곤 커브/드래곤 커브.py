import sys; input = sys.stdin.readline
from typing import List

R, U, L, D = range(4)
FIELD_HEIGHT = FIELD_WIDTH = 101


def make_dragon_curve(max_generation: int) -> List[int]:
    cache = [R]
    
    for _ in range(max_generation):
        for i in range(len(cache)-1, -1, -1):
            cache.append((cache[i]+1) % 4)
    
    return cache


def get_square(field: List[List[bool]]):
    result = 0
    
    for h in range(FIELD_HEIGHT-1):
        for w in range(FIELD_WIDTH-1):
            if field[h][w]\
                    and field[h][w+1]\
                    and field[h+1][w]\
                    and field[h+1][w+1]:
                result += 1

    return result            


curves = []
max_generation = 0
field = [[0] * FIELD_WIDTH for _ in range(FIELD_HEIGHT)]

for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    max_generation = max(max_generation, g)
    curves.append((x, y, d, g))

cache_dargon_curve = make_dragon_curve(max_generation)

for x, y, d, g in curves:
    field[y][x] = 1
    correction = d - R

    for i in range(2 ** g):
        direction = (cache_dargon_curve[i] + correction) % 4

        if direction == U:
            y -= 1
        elif direction == R:
            x += 1
        elif direction == D:
            y += 1
        elif direction == L:
            x -= 1
        else:
            print("Error")
        
        if (0 <= x < FIELD_WIDTH)\
                and (0 <= y < FIELD_HEIGHT):
            field[y][x] = 1

print(get_square(field))