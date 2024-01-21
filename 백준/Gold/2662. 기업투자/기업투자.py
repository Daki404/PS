import sys; input = sys.stdin.readline
from typing import List


def invest(company_idx: int, capacity: int) -> int:
    if company_idx == m\
            or company_idx < 0:
        return 0
    
    if (ret := cache[company_idx][capacity]):
        return ret
    
    ret = invest(company_idx+1, capacity)

    for money in range(1, capacity+1):
        ret = max(ret,
                  invest(company_idx+1, capacity-money)
                  + company_invest[money-1][company_idx])
    
    cache[company_idx][capacity] = ret
    return ret


def reconstruct(company_idx: int, capacity: int) -> None:
    if company_idx == m:
        return
    
    if invest(company_idx, capacity) == invest(company_idx+1, capacity):
        picked.append(0)
        reconstruct(company_idx+1, capacity)
    
    else:
        for i in range(1, capacity+1):
            if (company_invest[i-1][company_idx] + invest(company_idx+1, capacity-i))\
                    == invest(company_idx, capacity):
                picked.append(i)
                reconstruct(company_idx+1, capacity-i)
                break


n, m = map(int, input().split())

picked = []
cache = [[0] * (n+1) for _ in range(m)]
company_invest = [list(map(int, input().split()))[1:] for _ in range(n)]

print(invest(0, n))
reconstruct(0, n)
print(*picked)