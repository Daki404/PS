import sys; input = sys.stdin.readline


def get_minimum_cost(idx: int, visit: int) -> int:
    if idx == n:
        return 0
    
    if (ret := cache[idx][visit]):
        return ret
    
    ret = float('inf')
    for i in range(n):
        if visit & (1<<i):
            continue

        ret = min(ret, 
                  cost[idx][i] + get_minimum_cost(idx+1, visit | (1<<i)))

    cache[idx][visit] = ret
    return ret


n = int(input())

cache = [[None] * (2 << n) for _ in range(n)]
cost = [list(map(int, input().split())) for _ in range(n)]

print(get_minimum_cost(0, 0))