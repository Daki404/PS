import sys
from typing import List, Dict, Tuple
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def solve(n: int, board: List[List[int]]) -> int:
    def init_board() -> Dict:
        def set_board(x: int, y: int, color: str) -> None:
            x, y = x - 1, y + 1
            while x < n - 1 and y > 0:
                x += 1
                y -= 1
                b_w_diagonal[color][x-y+n-1] = True

        b_w_diagonal = defaultdict(dict)

        first_color = 'b' if n % 2 else 'w'
        second_color = 'w' if first_color == 'b' else 'b' 

        set_board(0, n - 1, first_color)
        set_board(0, n - 2, second_color)

        return b_w_diagonal

    def init_pos(st: int) -> Tuple[int, int]:
        x = st // 2
        y = st - x

        return x, y

    def dfs(st: int, color: str, cnt: int) -> None:
        if cnt + ((2*n - 1) // 2) <= max_counter[color]:
            return
        if st >= 2*n - 1:
            max_counter[color] = max(max_counter[color], cnt)
            return
        
        x, y = init_pos(st)
        x, y = x - 1, y + 1
        while (x < n - 1) and (0 < y):
            x += 1
            y -= 1
            down_right_diagonal = x - y + n - 1
            if board[y][x] \
                    and b_w_diagonal[color][down_right_diagonal]:
                b_w_diagonal[color][down_right_diagonal] = False
                dfs(st + 2, color, cnt + 1)
                b_w_diagonal[color][down_right_diagonal] = True

        x, y = init_pos(st)
        while (0 < x) and (y < n - 1):
            x -= 1
            y += 1
            down_right_diagonal = x - y + n - 1
            if board[y][x]\
                    and b_w_diagonal[color][down_right_diagonal]:
                b_w_diagonal[color][down_right_diagonal] = False
                dfs(st + 2, color, cnt + 1)
                b_w_diagonal[color][down_right_diagonal] = True

        dfs(st + 2, color, cnt)

    b_w_diagonal = init_board()
    max_counter = {'b': 0, 'w': 0}

    dfs(0, 'b', 0)
    dfs(1, 'w', 0)

    return sum(max_counter.values())


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, board))