import sys; input = sys.stdin.readline
from typing import List, Tuple

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

def min_diff_field():
    def bfs(x: int, y: int, num: int) -> int:
        score = 0
        stack = [(x, y)]
        
        while stack:
            x, y = stack.pop()
            
            if visit[y][x]:
                continue
            
            visit[y][x] = num
            score += field[y][x]
            
            for i in range(len(DX)):
                new_x = x + DX[i]
                new_y = y + DY[i]

                if not (0 <= new_x < n+2)\
                        or not (0 <= new_y < n+2)\
                        or visit[new_y][new_x]:
                    continue
                    
                stack.append((new_x, new_y))
        return score

    def get_coord_combination() -> List[Tuple[int]]:
        result = []

        for x in range(1, n-1):
            for y in range(2, n):
                for d1 in range(1, y):
                    for d2 in range(1, n-y+1):
                        if d1+d2 > n-x:
                            continue
                        result.append((x, y, d1, d2))

        return result

    result = float('inf')

    for x, y, d1, d2 in get_coord_combination():
        score = {i:0 for i in range(1, 6)}
        visit = [[0] * (n+2) for _ in range(n+2)]

        for i in range(d1+1):
            visit[y-i][x+i] = 5
            visit[y+d2-i][x+d2+i] = 5

        for i in range(d2+1):
            visit[y+i][x+i] = 5
            visit[y-d1+i][x+d1+i] = 5
        
        for i in range(y-d1):
            visit[i][x+d1] = 1
            score[1] += field[i][x+d1]
        for i in range(y+d2+1, len(visit)):
            visit[i][x+d2] = 4
            score[4] += field[i][x+d2]
        for i in range(x):
            visit[y][i] = 3
            score[3] += field[y][i]
        for i in range(x+d1+d2+1, len(visit)):
            visit[y+d2-d1][i] = 2
            score[2] += field[y+d2-d1][i]

        for i, coord in zip(range(1, 5),
                            [(x+d1-1, y-d1),
                             (x+d1+1, y-d1),
                             (x, y+1),
                             (x+d2+d1, y+d2-d1+1),
                             ]):
            score[i] += bfs(*coord, i)
        
        score[5] = total_sum - sum(score.values()) 
        scores = score.values()

        result = min(result, max(scores) - min(scores))
    
    return result
        

n = int(input())
field = [[0]+list(map(int, input().split()))+[0] for _ in range(n)]
field = [[0] * (n+2)] +  field + [[0] * (n+2)]
total_sum = sum(sum(field, []))

print(min_diff_field())