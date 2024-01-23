import sys; input = sys.stdin.readline

n = int(input())


for _ in range(n):
    boxes = []
    candies, box_cnt = map(int, input().split())
    
    for _ in range(box_cnt):
        r, c = map(int, input().split())
        boxes.append(r*c)

    boxes.sort(reverse=True)
    idx = 0

    while candies > 0:
        candies -= boxes[idx]
        idx += 1
    
    print(idx)