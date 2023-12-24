import sys; input = sys.stdin.readline
from typing import List
from copy import deepcopy

sys.setrecursionlimit(10**6)
SHARK = -1
BLANK = -2
DX = [0, -1, -1, -1, 0, 1, 1, 1]
DY = [-1, -1, 0, 1, 1, 1, 0, -1]


class SharkSimulation:
    def __init__(self, sea: List[List[List[int]]], mapper: dict[List[int]]) -> None:
        num, direct = sea[0][0]
        sea[0][0] = [SHARK, direct]
        del mapper[num]
        self.sea = sea
        self.fish_num_to_pos = mapper
        self.tmp_score = num
        self.max_score = num

    def fish_move(self) -> None:
        for num in range(1, 17):
            if not (pos := self.fish_num_to_pos.get(num, False)):
                continue
            
            y, x = pos
            num, direct = self.sea[y][x]
            for i in range(8):
                new_direct = (direct+i)%8
                new_y = y + DY[new_direct]
                new_x = x + DX[new_direct]

                if (0 <= new_x < 4)\
                        and (0 <= new_y < 4)\
                        and self.sea[new_y][new_x][0] != SHARK:
                    self.sea[y][x][1] = new_direct
                    new_num = self.sea[new_y][new_x][0]
                    self.sea[new_y][new_x], self.sea[y][x] = self.sea[y][x], self.sea[new_y][new_x]
                    
                    self.fish_num_to_pos[new_num] = [y, x]
                    self.fish_num_to_pos[num] = [new_y, new_x]
                    break            

    def next_shark_poses(self) -> List[List[int]]:
        possible_pos = []

        shark_pos = self.fish_num_to_pos[SHARK]
        shark_y, shark_x = shark_pos
        shark_direct = self.sea[shark_y][shark_x][1]

        shark_y += DY[shark_direct]
        shark_x += DX[shark_direct]

        while (0<=shark_y<4)\
                    and (0<=shark_x<4):
            if self.sea[shark_y][shark_x][0] != BLANK:
                possible_pos.append((shark_y, shark_x))
            shark_y += DY[shark_direct]
            shark_x += DX[shark_direct]

        return possible_pos

    def shark_dfs(self, i) -> None:
        self.fish_move()

        origin_shark_pos = self.fish_num_to_pos[SHARK]
        origin_shark_y, origin_shark_x = origin_shark_pos
        
        if not(next_poses := self.next_shark_poses()):
            self.max_score = max(self.max_score, self.tmp_score)
            return
        
        for shark_pos in next_poses:
            y, x = shark_pos
            
            origin_num_to_pos = deepcopy(self.fish_num_to_pos)
            origin_sea = deepcopy(self.sea)
            
            num, direct = self.sea[y][x]
            self.tmp_score += num
            self.sea[origin_shark_y][origin_shark_x] = [BLANK, BLANK]
            self.sea[y][x] = [SHARK, direct]
            self.fish_num_to_pos[SHARK] = [y, x]
            del self.fish_num_to_pos[num]  
            
            self.shark_dfs(i+1)

            self.fish_num_to_pos = origin_num_to_pos
            self.sea = origin_sea
            self.tmp_score -= num
    
    def print_sea(self, i):
        print("-----")
        print(f"d: {i}, score:{self.tmp_score}")
        print("-----")
        for i in self.sea:
            print(*i)
        print()

sea = [[[BLANK, BLANK] for _ in range(4)]for _ in range(4)]
fish_num_to_pos = {SHARK: [0, 0]}

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(0, 8, 2):
        num, direct = line[j], line[j+1]-1
        sea[i][j//2] = [num, direct]
        fish_num_to_pos[num] = [i, j//2]

game = SharkSimulation(sea, fish_num_to_pos)
game.shark_dfs(1)
print(game.max_score)