import sys
from typing import List

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def count_safe(field: List[List[int]]) -> int:
    def init_visit(threshold: int) -> List[List[bool]]:
        return [[False if field[i][j] > threshold else True \
                 for j in range(len(field))] \
                for i in range(len(field))]
        
    def dfs(x:int, y: int):
        nonlocal visit
        stack = [(x, y)]

        while stack:
            x, y = stack.pop()
            visit[y][x] = True

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if not (0 <= new_x < len(field)) \
                        or not (0 <= new_y < len(field)):
                    continue

                if visit[new_y][new_x]:
                    continue

                stack.append((new_x, new_y))

    max_result = 0
    min_height = min(map(min, *field))
    max_height = max(map(max, *field))

    for i in range(min_height - 1, max_height):
        visit = init_visit(i)
        result = 0
        
        for h in range(len(field)):
            for w in range(len(field)):
                if visit[h][w]:
                    continue
                
                result += 1 
                dfs(w, h)
        
        max_result = max(max_result, result)

    return max_result


n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

print(count_safe(field))