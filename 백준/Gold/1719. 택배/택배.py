import sys; input = sys.stdin.readline
from typing import List
from copy import deepcopy


def flyod_washall(move_table: List[List[int]]) -> List[List[int]]:
    for mid in range(n):
        for st in range(n):
            for ed in range(n):
                if st == ed:
                    continue

                new_cost = cost[st][mid] + cost[mid][ed]
                
                if new_cost < cost[st][ed]:
                    cost[st][ed] = new_cost
                    move_table[st][ed] = move_table[st][mid]
    
    return move_table               


n, m = map(int, input().split())

cost = [[float('inf')] * n for _ in range(n)]
move_table = [[-1] * n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0

for _ in range(m):
    st, ed, dis = map(int, input().split())
    st -= 1; ed -= 1
    cost[st][ed] = cost[ed][st] = dis
    move_table[st][ed] = ed
    move_table[ed][st] = st

road_cost = flyod_washall(move_table)

for i in road_cost:
    for j in i:
        if j == -1:
            print("-", end=" ")
        else:
            print(j+1, end=" ")
    print()