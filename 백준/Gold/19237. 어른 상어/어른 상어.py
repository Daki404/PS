import sys; input = sys.stdin.readline;

U, D, L, R = range(1, 5)
DIRECT_MAPPER = {
                    U: (0, -1),
                    D: (0, 1),
                    L: (-1, 0),
                    R: (+1, 0),
                }


def drcrease_smell() -> None:
    for h in range(sea_size):
        for w in range(sea_size):
            if smell_sea[h][w] is None:
                continue
            num, turn = smell_sea[h][w]
            turn -= 1

            if not turn:
                smell_sea[h][w] = None
            else:
                smell_sea[h][w] = (num, turn)


def shark_move() -> int:
    for num in range(1, shark_cnt+1):
        if num not in shark_pos:
            continue

        y, x, direct = shark_pos[num]

        my_area_pos = None
        for next_direct in shark_direction[num][direct]:
            new_x, new_y = DIRECT_MAPPER[next_direct]
            new_x += x
            new_y += y

            if not(0<=new_x<sea_size)\
                    or not(0<=new_y<sea_size)\
                    or (smell_sea[new_y][new_x] is not None\
                    and smell_sea[new_y][new_x][0] != num):
                continue

            if smell_sea[new_y][new_x] is None:
                shark_pos[num] = (new_y, new_x, next_direct)
                break

            if my_area_pos is None:
                my_area_pos = (new_y, new_x, next_direct)
        else:
            if my_area_pos is not None:
                shark_pos[num] = my_area_pos
    
    for shark_num in range(shark_cnt, 0, -1):
        if shark_num not in shark_pos:
            continue

        y, x, _ = shark_pos[shark_num]
        
        if smell_sea[y][x] is not None\
                and smell_sea[y][x][0] != shark_num:
            num, _ = smell_sea[y][x]
            del shark_pos[num]
        
        smell_sea[y][x] = (shark_num, smell+1)

    return 1
    
            
def shark_simulation() -> int:
    att = 0
    while att <= 1000:
        if len(shark_pos) == 1:
            return att
        
        att += shark_move()
        drcrease_smell()
    return -1



sea_size, shark_cnt, smell = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(sea_size)]
smell_sea = [[None] * sea_size for _ in range(sea_size)]


shark_pos = {}
shark_direction = {shark_num: dict() for shark_num in range(1, shark_cnt+1)}
for h in range(sea_size):
    for w in range(sea_size):
        if not sea[h][w]:
            continue
        shark_num = sea[h][w] 
        shark_pos[shark_num] = [h, w]
        smell_sea[h][w] = (shark_num, smell)

for idx, direct in enumerate(map(int, input().split())):
    shark_pos[idx+1].append(direct)

for i in range(1, shark_cnt+1):
    shark_direction[i][U] = list(map(int, input().split()))
    shark_direction[i][D] = list(map(int, input().split()))
    shark_direction[i][L] = list(map(int, input().split()))
    shark_direction[i][R] = list(map(int, input().split()))

print(shark_simulation())