import sys
from typing import List

input = sys.stdin.readline


def validate_game(score: List[int]) -> int:
    def dfs(x: int, y:int) -> None:
        nonlocal result

        if x >= 5:
            if not sum(score_dict[5].values()):
                result = 1     
            return 
        
        if y > 5:
            dfs(x + 1, x + 2)
            return
        
        for i, j in zip(["win", "draw", "lose"], ["lose", "draw", "win"]):
            if score_dict[x][i] and score_dict[y][j]:
                score_dict[x][i] -= 1
                score_dict[y][j] -= 1
                
                dfs(x, y + 1)

                score_dict[x][i] += 1
                score_dict[y][j] += 1

    result = 0
    score_dict = []
    total_win = total_draw = total_lose = 0
    
    for i in range(0, len(score), 3):
        if sum(score[i: i+3]) != 5:
            return result
        
        total_win += score[i]
        total_draw += score[i + 1]
        total_lose += score[i + 2]

        score_dict.append({'win': score[i], 'draw': score[i + 1], 'lose': score[i + 2]})
    
    if total_win != total_lose \
            or total_draw % 2:
        return result
    
    dfs(0, 1)
    return result
    

for _ in range(4):
    line = list(map(int, input().split()))
    print(validate_game(line))