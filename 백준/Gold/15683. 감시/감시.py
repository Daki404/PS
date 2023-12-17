import sys

input = sys.stdin.readline
EMPTY, ONE, LINE, ANGLE, TRIANGLE, FULL, WALL = range(7)
CCTV_DIRECT = {
            ONE: ('U', 'D', "L", "R"),
            LINE: ('UD', 'LR'),
            ANGLE: ('UL', 'LD', 'DR', 'UR'),
            TRIANGLE: ('UDL', 'UDR', 'ULR', 'DLR'),
            FULL: ('ULDR')
}

def straight_watch(x: int, y:int, direct:str, add:bool) -> int:
    if direct == 'U': y -= 1
    elif direct == 'D': y += 1
    elif direct == 'R': x += 1
    elif direct == 'L': x -= 1
    
    result = 0
    while (0 <= x < w)\
                and (0 <= y < h)\
                and field[y][x] != WALL:
        if add:
            if field[y][x] == EMPTY:
                field[y][x] -= 1
                result += 1
    
            elif field[y][x] < EMPTY:
                field[y][x] -= 1
        else:
            if field[y][x] < EMPTY:
                field[y][x] += 1
                
                if field[y][x] == EMPTY:
                    result += 1
                
        if direct == 'U': y -= 1
        elif direct == 'D': y += 1
        elif direct == 'R': x += 1
        elif direct == 'L': x -= 1
    
    return result


def watch_area(x: int, y: int, cctv_direct: str) -> int:
    result = 0
    for direction in list(cctv_direct):
        result += straight_watch(x, y, direction, True)

    return result


def clean_area(x: int, y: int, cctv_direct: str) -> int:
    result = 0
    for direction in list(cctv_direct):
        result += straight_watch(x, y, direction, False)
    
    return result


def max_watch_area(cctv_idx: int) -> int:
    if cctv_idx >= len(cctv_list):
        return 0
    
    x, y = cctv_list[cctv_idx]
    max_area = 0

    for direction in CCTV_DIRECT[field[y][x]]:
        result = watch_area(x, y, direction)
        result += max_watch_area(cctv_idx+1)
        max_area = max(max_area, result)

        result -= clean_area(x, y, direction)
    
    return max_area


square_area = 0
h, w = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(h)]
cctv_list = []

for i in range(h):
    for j in range(w):
        if field[i][j] == FULL:
            square_area -= watch_area(j, i, CCTV_DIRECT[FULL])
        elif field[i][j] in (ONE, LINE, ANGLE, TRIANGLE):
            cctv_list.append((j, i))
        elif field[i][j] != WALL:
            square_area += 1

print(square_area - max_watch_area(cctv_idx=0))