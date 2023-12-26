import sys; input = sys.stdin.readline
from typing import Tuple, Dict
from collections import deque


WALL = 1
DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


def init_customer(customers: Dict[Tuple, Tuple]):
    customer_cost = {i: float('inf') for i in customers}

    for st, ed in customers.items():
        st_x, st_y = st
        ed_x, ed_y = ed
        
        queue = deque([(st_x, st_y)])
        visited = [[0] * field_len for _ in range(field_len)]
        visited[st_y][st_x] = 1

        while queue:
            x, y = queue.popleft()

            if x == ed_x\
                    and y == ed_y:
                customer_cost[st] = visited[ed_y][ed_x] - 1
                break
            
            for dx, dy in zip(DX, DY):
                new_x = x + dx
                new_y = y + dy

                if not(0<= new_x<field_len)\
                        or not(0<=new_y<field_len)\
                        or field[new_y][new_x] == WALL\
                        or visited[new_y][new_x]:
                    continue

                visited[new_y][new_x] = visited[y][x] + 1
                queue.append((new_x, new_y))
    
    return customer_cost


def get_next_customer(x: int, y:int):
    distance_customer = []
    queue = deque([(x, y)])

    visited = [[0] * field_len for _ in range(field_len)]
    visited[y][x] = 1

    while queue:
        x, y = queue.popleft()
        if (x, y) in customers:
            distance_customer.append((x, y, visited[y][x]))
        
        if len(distance_customer) == len(customers):
            break

        for dx, dy in zip(DX, DY):
            new_x = x + dx
            new_y = y + dy

            if not(0<= new_x<field_len)\
                    or not(0<=new_y<field_len)\
                    or field[new_y][new_x] == WALL\
                    or visited[new_y][new_x]:
                continue

            visited[new_y][new_x] = visited[y][x] + 1
            queue.append((new_x, new_y))
    
    if not distance_customer:
        return None
    
    return min(distance_customer, key=lambda x:(x[2], x[1], x[0]))



field_len, customer_cnt, fuel = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(field_len)]

taxi_y, taxi_x = map(int, input().split())
taxi_x -= 1
taxi_y -= 1

customers = dict()
for _ in range(customer_cnt):
    st_y, st_x, ed_y, ed_x = map(int, input().split())
    customers[(st_x-1, st_y-1)] = (ed_x-1, ed_y-1)

customer_cost = init_customer(customers)

while len(customers):
    if (next_customer := get_next_customer(taxi_x, taxi_y)) is None:
        print(-1)
        break
    
    x, y, cost = next_customer
    cost -= 1

    if cost + customer_cost[(x, y)] > fuel:
        print(-1)
        break
    
    fuel = fuel - cost + customer_cost[(x, y)]
    taxi_x, taxi_y = customers[(x, y)]
    del customers[(x, y)]
    
else: # 손님 다 태움
    print(fuel)