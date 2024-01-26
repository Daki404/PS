import sys; input = sys.stdin.readline
from typing import List, Dict
from heapq import heappop, heappush
from collections import defaultdict


def dijkstra(st_node: int) -> Dict[int, int]:
    minimum_cost = {node:[float('inf'), False] for node in range(nodes)}
    minimum_cost[st_node] = (0, False)
    next_node = [(0, st_node, False)]

    while next_node:
        cost, node, used = heappop(next_node)

        if cost > minimum_cost[node][0]:
            continue

        for new_node, new_cost in road_connect[node].items():
            tmp_used = used
            new_cost += cost

            if new_cost > minimum_cost[new_node][0]:
                continue

            if (node == road_st and new_node == road_ed)\
                    or (node == road_ed and new_node == road_st):
                tmp_used = True

            if minimum_cost[new_node][0] > new_cost:
                minimum_cost[new_node] = (new_cost, tmp_used)
                heappush(next_node, (new_cost, new_node, tmp_used))
            
            elif not minimum_cost[new_node][1] and tmp_used:
                minimum_cost[new_node] = (new_cost, tmp_used)
                heappush(next_node, (new_cost, new_node, tmp_used))
    
    return minimum_cost


for _ in range(int(input())):
    nodes, roads, ends = map(int, input().split())
    st_node, road_st, road_ed = map(lambda x: int(x)-1, input().split())

    road_connect = defaultdict(dict)

    for i in range(roads):
        st, ed, length = map(int, input().split())
        st -= 1; ed -= 1

        length = min(road_connect[st].get(ed, float('inf')), length)
        road_connect[st][ed] = length 
        road_connect[ed][st] = length

    cost = dijkstra(st_node)
    
    result = []
    for i in range(ends):
        node = int(input())
        
        if cost[node-1][1]:
            result.append(node)
    
    print(*sorted(result))