import sys; input = sys.stdin.readline
from collections import defaultdict

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

n = int(input())
field = [[False] * n for _ in range(n)]
prefer = defaultdict(list)

for _ in range(n**2):
    line = list(map(int, input().split()))
    prefer[line[0]] += line[1:]

for student, favorites in prefer.items():
    max_favorite = max_blank = -1

    for h in range(n):
        for w in range(n):
            if field[h][w]:
                continue

            tmp_favorite = tmp_blank = 0
            for dx, dy in zip(DX, DY):
                x = w + dx
                y = h + dy

                if not(0<=x<n)\
                        or not(0<=y<n):
                    continue

                if field[y][x] in favorites:
                    tmp_favorite += 1
                
                elif not field[y][x]:
                    tmp_blank += 1

            if max_favorite < tmp_favorite:
                max_favorite = tmp_favorite
                max_blank = tmp_blank
                queue = [(h, w)]

            elif max_favorite == tmp_favorite:
                if max_blank < tmp_blank:
                  max_blank = tmp_blank
                  queue = [(h, w)]

                elif max_blank == tmp_blank:
                    queue.append((h, w))
    h, w = queue[0]
    field[h][w] = student

result = 0
weights = [0, 1, 10, 100, 1000]
for h in range(n):
    for w in range(n):
        tmp = 0
        student = field[h][w]

        for dx, dy in zip(DX, DY):
            x = w + dx
            y = h + dy

            if not(0<=x<n)\
                    or not(0<=y<n):
                continue

            if field[y][x] in prefer[student]:
                tmp += 1
        
        result += weights[tmp]

print(result)