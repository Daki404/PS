import sys; input = sys.stdin.readline
from copy import deepcopy
from collections import deque
from typing import List
from itertools import combinations

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]
BLANK, WALL, PASSIVE_VIRUS, ACTIVE_VIRUS = range(0, 4)


def minimim_posioned() -> int:
    def bfs(st_virus_idx: List[int]) -> int:
        lab = deepcopy(field)
        lab_blank = blank_cnt

        queue = deque()
        for i in st_virus_idx:
            x, y = virus_pos[i]
            queue.append((x, y, 1))
            lab[y][x] = ACTIVE_VIRUS

        while queue:
            x, y, time = queue.popleft()

            for dx, dy in zip(DX, DY):
                new_x = x + dx
                new_y = y + dy

                if not(0<=new_x<lab_size) \
                        or not(0<=new_y<lab_size)\
                        or lab[new_y][new_x] == WALL\
                        or lab[new_y][new_x] == ACTIVE_VIRUS:
                    continue

                if lab[new_y][new_x] == BLANK:
                    lab_blank -= 1
                    
                    if not lab_blank:
                        return time
                
                lab[new_y][new_x] = ACTIVE_VIRUS
                queue.append((new_x, new_y, time + 1))
        
        return float('inf')
    
    min_time = float('inf')
    for viruses in combinations(range(len(virus_pos)), st_virus_cnt):
        min_time = min(min_time, bfs(viruses))
    
    return min_time if min_time != float('inf') else -1


lab_size, st_virus_cnt = map(int, input().split())
blank_cnt = 0
field = []
virus_pos = []

for h in range(lab_size):
    line = list(map(int, input().split()))
    for idx, val in enumerate(line):
        if val == PASSIVE_VIRUS:
            virus_pos.append((idx, h))
        elif val == BLANK:
            blank_cnt += 1
    field.append(line)

if not blank_cnt:
    print(0)
else:
    print(minimim_posioned())