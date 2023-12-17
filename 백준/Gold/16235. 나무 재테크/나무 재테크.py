import sys; input = sys.stdin.readline
from collections import deque

DX = [-1, 0, 1, 1, 1, 0, -1, -1]
DY = [1, 1, 1, 0, -1, -1, -1, 0]


def seaon_cycle() -> None:
    born_tree = []
    # Spring & Summer
    for h in range(farm_size):
        for w in range(farm_size):
            next_seaon_tree = deque()
            dead_tree = 0

            while farm[h][w]:
                tree = farm[h][w].popleft()

                if tree <= energy[h][w]:
                    energy[h][w] -= tree
                    tree += 1
                    next_seaon_tree.append(tree)

                    if (tree % 5) == 0:
                        born_tree.append((h, w))

                else:
                    dead_tree += (tree//2)

            farm[h][w] = next_seaon_tree
            energy[h][w] += dead_tree
    
    # Fall
    for h, w in born_tree:
        for dw, dh in zip(DX, DY):
            new_h = h + dh
            new_w = w + dw

            if not(0<=new_w<farm_size)\
                    or not(0<=new_h<farm_size):
                continue
            
            farm[new_h][new_w].appendleft(1)

    # Winter
    for h in range(farm_size):
        for w in range(farm_size):
            energy[h][w] += energy_apply[h][w]


def survive_tree() -> int:
    result = 0

    for h in range(farm_size):
        for w in range(farm_size):
            result += len(farm[h][w])
    
    return result


farm_size, tree_cnt, year = map(int, input().split())
farm = [[deque() for _ in range(farm_size)] for _ in range(farm_size)]
energy = [[5] * farm_size for _ in range(farm_size)]
energy_apply = [list(map(int, input().split())) for _ in range(farm_size)]


for _ in range(tree_cnt):
    x, y, old = map(int, input().split())
    farm[x-1][y-1].append(old)

for _ in range(year):
    seaon_cycle()

print(survive_tree())