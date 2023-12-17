import sys

input = sys.stdin.readline

U = 0
R = 2
L = 6
CW = 1
CCW = -1

gears = [input().strip() for _ in range(4)]


def spin(gear_idx: int, direct: int, chain_direct:int) -> None:
    origin_gear_idx = gear_idx

    if chain_direct == L:
        gear_idx -= 1

    elif chain_direct == R:
        gear_idx += 1


    if not (0 <= gear_idx < 4):
        return
    
    if spined_state[gear_idx]:
        return

    if chain_direct == L \
            and gears[gear_idx][R] == gears[origin_gear_idx][L]:
        return
    
    if chain_direct == R \
            and gears[gear_idx][L] == gears[origin_gear_idx][R]:
        return
    
    spined_state[gear_idx] = True

    spin(gear_idx, -direct, L)
    spin(gear_idx, -direct, R)
    
    # 우측 시프트
    if direct == CW:
        gears[gear_idx] = gears[gear_idx][-1] + gears[gear_idx][:-1]
    
    # 좌측 시프트
    else:   # CCW
        gears[gear_idx] = gears[gear_idx][1:] + gears[gear_idx][0]


def measure_gear():
    result = 0
    weight = 1

    for i in range(4):
        if gears[i][U] == '1':
            result += weight
        weight *= 2
    
    return result

for _ in range(int(input())):
    gear_idx, direct = map(int, input().split())
    spined_state = [False] * 4
    spin(gear_idx - 1, direct, None)

print(measure_gear()) 