import sys; input = sys.stdin.readline
from typing import List


def prefix_sum(idx: int) -> int:
    res = 0

    while idx > 0:
        res += fenwick_tree[idx]
        idx -= -idx&idx
    return res


def update(idx: int, diff: int) -> None:
    while idx <= n:
        fenwick_tree[idx] += diff
        idx += -idx&idx


def get_sum(st_idx: int, ed_idx: int) -> int:
    return prefix_sum(ed_idx) - prefix_sum(st_idx-1)


n, m = map(int, input().split())
arr = [0] * (n+1)
fenwick_tree = [0] * (n+1)

for _ in range(m):
    cmd, st, ed = map(int, input().split())

    if cmd == 0:
        st, ed = min(st, ed), max(st, ed)
        print(get_sum(st, ed))
    else:
        update(st, ed-arr[st])
        arr[st]=ed