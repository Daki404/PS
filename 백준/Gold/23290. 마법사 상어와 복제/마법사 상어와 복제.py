import sys; input = sys.stdin.readline
from collections import defaultdict
from typing import List, Dict, Tuple
from copy import deepcopy


DX = [-1, -1, 0, 1, 1, 1, 0, -1]
DY = [0, -1, -1, -1, 0, 1, 1, 1]


def move_fish(turn: int) -> Dict[Tuple, List[int]]:
    new_fish_info = defaultdict(lambda: defaultdict(int))

    for pos, fishs in fish_info.items():
        y, x = pos
        for fish in fishs:
            for i in range(8):
                new_d = (fish+8-i)%8 
                new_y = y + DY[new_d]
                new_x = x + DX[new_d]

                if not(0<=new_x<4)\
                        or not(0<=new_y<4)\
                        or (new_x == shark_x and new_y == shark_y)\
                        or (turn - sea[new_y][new_x]) <= 2:
                    continue
                
                new_fish_info[(new_y, new_x)][new_d] += fishs[fish]
                break
            else:
                new_fish_info[(y, x)][fish] += fishs[fish]
    return new_fish_info


def move_shark(turn: int) -> Tuple[int]:
    # BFS 로 확인하고 움직임 sea에다가 상어 위치 피 냄새 갬싱
    def dfs(y: int, x: int, distance: int) -> None:
        nonlocal shark_pos, catched_fish, optimal_fish, tmp_pos, max_cnt, cnt

        if distance == 0:
            if tmp_pos == (shark_y, shark_x): tmp_pos = (y, x)
            if cnt > max_cnt:
                max_cnt = cnt
                shark_pos = (y, x)
                optimal_fish = deepcopy(catched_fish)
            return
        
        for i in (2, 0, 6, 4):
            new_y = y + DY[i]
            new_x = x + DX[i]

            if not(0<=new_x<4)\
                    or not(0<=new_y<4):
                continue
            
            # 방문처리, 경로 추가, 물고기 삭제
            catch_fish = new_fish_info.pop((new_y, new_x), {}) 

            for fish in catch_fish:
                catched_fish.append((new_y, new_x, fish, catch_fish[fish]))
                cnt += catch_fish[fish]
            
            dfs(new_y, new_x, distance-1)
            
            for _ in range(len(catch_fish)):
                cnt -= catched_fish.pop()[-1]
      
            for new_d, new_c in catch_fish.items():
                new_fish_info[(new_y, new_x)][new_d] = new_c

    shark_pos = None
    cnt = 0
    max_cnt = 0
    tmp_pos = (shark_y, shark_x)
    optimal_fish = []
    catched_fish = []

    dfs(shark_y, shark_x, 3)

    # 최적의 경우에 물고기 피 비린내 처리
    for pos in optimal_fish:
        y, x, _, _ = pos
        sea[y][x] = turn
        new_fish_info[(y, x)] = defaultdict(int)
    
    return shark_pos if shark_pos is not None else tmp_pos


def update_fishes() -> None:
    for pos, fishes in new_fish_info.items():
        for fish in fishes:
            fish_info[pos][fish] += fishes[fish]


sea = [[-5] * 4 for _ in range(4)]
fish_cnt, spell_cnt = map(int, input().split())
fish_info = defaultdict(lambda: defaultdict(int))

for _ in range(fish_cnt):
    y, x, d = map(int, input().split())
    fish_info[(y-1, x-1)][d-1] += 1

shark_y, shark_x = map(int, input().split())
shark_x -= 1
shark_y -= 1

for i in range(spell_cnt):
    new_fish_info = move_fish(i)
    shark_y, shark_x = move_shark(i)
    update_fishes()

result = 0
for pos, info in fish_info.items():
    for fish in info.values():
        result += fish

print(result)
