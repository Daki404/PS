import sys; input = sys.stdin.readline
from typing import List
from collections import deque


DX = [-1, -1, 0, 1, 1, 1, 0, -1]
DY = [0, -1, -1, -1, 0, 1, 1, 1]


def move_cloud(direct: int, distance: int) -> List[List[int]]:
    dx = DX[direct] * distance
    dy = DY[direct] * distance

    for row in cloud:
        row.rotate(dx)

    for w in range(size):
        line = [cloud[i][w] for i in range(size)]
    
        for i in range(size):
            cloud[(i+dy+size)%size][w] = line[i]

    cloud_pos = []
    for h in range(size):
        for w in range(size):
            if cloud[h][w]:
                cloud_pos.append((w, h))
                field[h][w] += 1
                cloud[h][w] = 0

    return cloud_pos


def duplicate_water(last_cloud: List[List[int]]) -> None:
    update_pos = dict()

    for x, y in last_cloud:
        water = 0
        for dx, dy in zip((-1, 1, 1, -1), (-1, -1, 1, 1)):
            new_x = x + dx
            new_y = y + dy

            if not(0<=new_x<size)\
                    or not(0<=new_y<size)\
                    or field[new_y][new_x] == 0:
                continue

            water += 1
        update_pos[(x, y)] = water
    
    for pos, water in update_pos.items():
        x, y = pos
        field[y][x] += water


def make_cloud(last_cloud: List[List[int]]) -> None:
    for h in range(size):
        for w in range(size):
            if (w, h) in last_cloud\
                    or field[h][w] < 2:
                continue
            
            field[h][w] -= 2
            cloud[h][w] = 1


size, cmd_cnt = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(size)]
cloud = [deque([0] * size) for _ in range(size)]
cloud[size-1][0] = cloud[size-1][1] = cloud[size-2][0] = cloud[size-2][1] = 1


for _ in range(cmd_cnt):
    direct, distance = map(int, input().split())
    last_cloud = move_cloud(direct-1, distance)
    duplicate_water(last_cloud)
    make_cloud(last_cloud)

print(sum(map(sum, field)))