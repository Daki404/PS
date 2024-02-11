import sys; input = sys.stdin.readline

sys.setrecursionlimit(10**9)


def move_cost(st: int, ed: int) -> int:
    if st == ed:
        return 1
    
    if st == 0:
        return 2
    
    if abs(st - ed) == 2:
        return 4
    
    return 3

def solve(idx: int, foot: tuple[int]) -> int:
    if cmds[idx] == 0:
        return 0
    
    if (ret := cache.get((idx, foot))):
        return ret
    
    ret = move_cost(foot[0], cmds[idx]) + solve(idx+1, (cmds[idx], foot[1]))
    ret = min(ret,
              move_cost(foot[1], cmds[idx]) + solve(idx+1, (foot[0], cmds[idx])))
    

    cache[(idx, foot)] = ret
    return ret


cache = {}
cmds = list(map(int, input().split()))
print(solve(0, (0, 0)))