import sys; input = sys.stdin.readline
from math import ceil

plank_cnt, plank_length = map(int, input().split())

planks = [list(map(int, input().split())) for _ in range(plank_cnt)]
planks.sort(key=lambda x: (x[1], x[0]))

used_cnt = 0
used_len = 0

for st, ed in planks:
    st = max(used_len, st)
    
    if st >= ed:
        continue

    new_cnt = ceil((ed-st) / plank_length)
    used_cnt += new_cnt
    used_len = st + new_cnt*plank_length

print(used_cnt)