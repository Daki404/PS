import sys; input = sys.stdin.readline
from collections import deque


DX = [-1, -1, 0, 1, 1, 1, 0, -1]
DY = [0, 1, 1, 1, 0, -1, -1, -1]


fireballs = deque()
n, m, k = map(int, input().split())

for _ in range(m):
    r, c, m, s, d = list(map(int, input().split()))
    fireballs.append([r-1, c-1, m, s, d])

field = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(k):
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.popleft()
        nr = (cr + cs * DX[cd]) % n
        nc = (cc + cs * DY[cd]) % n
        field[nr][nc].append([cm, cs, cd])
    
    for r in range(n):
        for c in range(n):
            if len(field[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(field[r][c])
                while field[r][c]:
                    m, s, d = field[r][c].pop(0)
                    sum_m += m
                    sum_s += s
                    if d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                
                if sum_m // 5:
                    for d in nd:
                        fireballs.append([r, c, sum_m//5, sum_s//cnt, d])

            elif len(field[r][c]) == 1:
                fireballs.append([r, c] + field[r][c].pop())

print(sum([f[2] for f in fireballs]))