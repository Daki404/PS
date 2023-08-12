import sys
from dataclasses import dataclass
from collections import Counter

@dataclass
class Dot:
    x: int
    y: int


@dataclass
class Line:
    st: Dot
    ed: Dot


def judge_cross(a: Line, b: Line):
    def ccw(a: Dot, b: Dot, c: Dot) -> int:
        result = (a.x*b.y + b.x*c.y + c.x*a.y) \
                - (a.x*c.y + b.x*a.y + c.x*b.y)

        return result
    
    result_1 = ccw(a.st, a.ed, b.st) * ccw(a.st, a.ed, b.ed)
    result_2 = ccw(b.st, b.ed, a.st) * ccw(b.st, b.ed, a.ed)

    if result_1 == 0 and result_2 == 0:
        return min(a.st.x, a.ed.x) <= max(b.st.x, b.ed.x) \
            and max(a.st.x, a.ed.x) >= min(b.st.x, b.ed.x) \
            and min(a.st.y, a.ed.y) <= max(b.st.y, b.ed.y) \
            and max(a.st.y, a.ed.y) >= min(b.st.y, b.ed.y)
    
    return result_1 <= 0 and result_2 <= 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

lines = []
parent = [i for i in range(n)]

for _ in range(n):
    st_x, st_y, ed_x, ed_y = map(int, input().split())
    st, ed = Dot(st_x, st_y), Dot(ed_x, ed_y)
    line = Line(st, ed)
    lines.append(line)

for i in range(n - 1):
    for j in range(i + 1, n):
        if judge_cross(lines[i], lines[j]):
            union(i, j)

result = Counter([find(i) for i in parent])
print(len(result), max(result.values()), sep='\n')