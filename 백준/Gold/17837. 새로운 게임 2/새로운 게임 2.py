import sys; input = sys.stdin.readline

WHITE, RED, BLUE = range(3)
R, L, U, D = range(1, 5)


def turn_game():
    for i in range(1, obj_cnt+1):
        old_x, old_y, old_direct = obj_coord[i]
        x, y, direct, color = move(old_x, old_y, old_direct)
        """
        if old_x == x and old_y == y:
            continue
        """
        i_idx = obj_board[old_y][old_x].index(i)
        move_objs = obj_board[old_y][old_x][i_idx:]
        obj_board[old_y][old_x] = obj_board[old_y][old_x][:i_idx]

        if color == RED:
            move_objs = move_objs[::-1]
        
        obj_coord[i] = (x, y, direct)
        
        for j in move_objs:
            if j != i:
                _, _, obj_direct = obj_coord[j]
                obj_coord[j] = (x, y, obj_direct)
            obj_board[y][x].append(j)

            if len(obj_board[y][x]) >= 4:
                return True
    return False


def move(x, y, direct):
    if direct == R:
        weight = (1, 0)
    elif direct == L:
        weight = (-1, 0)
    elif direct == U:
        weight = (0, -1)
    else: #direct == D
        weight = (0, 1)
    
    x += weight[0]
    y += weight[1]
    
    now_color = color_board[y][x]

    if now_color == BLUE:
        x -= weight[0]*2
        y -= weight[1]*2
        direct = flip_direct(direct)
        now_color = color_board[y][x]

        if now_color == BLUE:
            x += weight[0]
            y += weight[1]

    return x, y, direct, now_color
    


def flip_direct(direct):
    if direct == R:
        return L
    elif direct == L:
        return R
    elif direct == U:
        return D
    else:
        return U


board_size, obj_cnt = map(int, input().split())
color_board = [[BLUE] * (board_size+2)]\
                + [[BLUE] + list(map(int, input().split()))+ [BLUE] for _ in range(board_size)]\
                + [[BLUE] * (board_size+2)]
obj_board = [[list() for _ in range(board_size+2)] for _ in range(board_size+2)]
obj_coord = dict()


for i in range(1, obj_cnt+1):
    row, col, direct = map(int, input().split())
    obj_coord[i] = [col, row, direct]
    obj_board[row][col].append(i)

now_turn = 1
while now_turn <= 1000:
    if turn_game():
        print(now_turn)
        break
    now_turn += 1

else:
    print(-1)