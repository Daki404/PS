import sys; input = sys.stdin.readline
from collections import Counter
from itertools import chain


def minimum_calc(r: int, c: int, k: int) -> None:
    def dfs(time: int):
        if time > 100:
            return -1

        if field[r-1][c-1] == k:
            return time

        if max_row >= max_col:
            R_calc()
        else:
            C_calc()
        
        return dfs(time+1)
    
    def R_calc():
        nonlocal max_col

        for h in range(max_row+1):
            row = []
            for w in range(max_col+1):
                if not field[h][w]:
                    continue
                row.append(field[h][w])

            counter = Counter(row)
            order = sorted(counter.items(), key=lambda pair:(pair[1],pair[0]))
            line = list(chain(*order))
            max_col = max(max_col, len(line)-1)

            for w in range(min(max_col+1, 100)):
                if w < len(line):
                    field[h][w] = line[w]
                else:
                    field[h][w] = 0

    def C_calc():
        nonlocal max_row

        for w in range(max_col + 1):
            col = []
            for h in range(max_row+1):
                if not field[h][w]:
                    continue
                col.append(field[h][w])
            
            counter = Counter(col)
            order = sorted(counter.items(), key=lambda pair:(pair[1],pair[0]))
            line = list(chain(*order))
            max_row = max(max_row, len(line)-1)

            for h in range(min(max_row+1, 100)):
                if h < len(line):
                    field[h][w] = line[h]
                else:
                    field[h][w] = 0 
    
    max_row = max_col = 2
    return dfs(time=0)
        


field = [[0] * 100 for _ in range(100)]
r, c, k = map(int, input().split())

for i in range(3):
    line = map(int, input().split())
    field[i][0], field[i][1], field[i][2] = line

print(minimum_calc(r, c, k))