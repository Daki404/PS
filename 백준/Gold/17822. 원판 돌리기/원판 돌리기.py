import sys; input = sys.stdin.readline
from collections import deque


CW = 0
CCW = 1


def spin(plane_num: int, direction:int, att:int) -> None:
    if direction == CW:
        distance = att
    else: # direction == CCW
        distance = -att

    planes[plane_num].rotate(distance)


def clear() -> bool:
    death_set = set()

    for i in range(1, len(planes)-1):
        for j in range(plane_len):
            now = planes[i][j]
            
            if now == 0:
                continue

            if planes[i][j-1] == now:
                death_set.add((i, j-1))
                death_set.add((i, j))

            if now == planes[i][(j+1)%plane_len]:
                death_set.add((i, j))
                death_set.add((i, (j+1)%plane_len))
            
            if now == planes[i+1][j]:
                death_set.add((i, j))
                death_set.add((i+1, j))

            if now == planes[i-1][j]:
                death_set.add((i, j))
                death_set.add((i-1, j))
    
    for h, w in death_set:
        planes[h][w] = 0 
    
    return len(death_set)


def correction_plane():
    total_sum = 0
    total_cnt = 0
    for i in range(1, len(planes)-1):
        for j in range(plane_len):
            if planes[i][j]:
                total_cnt += 1
            total_sum += planes[i][j]
    
    if not total_cnt:
        return False
    
    avg = total_sum / total_cnt
    for i in range(1, len(planes)-1):
        for j in range(plane_len):
            if not planes[i][j]:
                continue
            
            if planes[i][j] > avg:
                planes[i][j] -= 1
            
            elif planes[i][j] < avg:
                planes[i][j] += 1


def sum_plane():
    return sum(map(sum, planes))
                

plane_num, plane_len, att = map(int, input().split())
planes = [deque([0] * plane_len)]\
        + [deque(map(int, input().split())) for _ in range(plane_num)]\
        + [deque([0] * plane_len)]

for _ in range(att):
    x, d, k = map(int, input().split())
    
    for i in range(x, len(planes)-1, x):
        spin(i, d, k)

    if not clear():
        correction_plane()

print(sum_plane()) 