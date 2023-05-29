from typing import List
import sys

INF = float('inf')
input = sys.stdin.readline


def solve(n: int, path: List[List[int]]) -> int:
    dp = [[0] * (1 << (n-1)) for _ in range(n)]
    st_node = 0

    def dfs(node: int, log: int) -> int:
        if dp[node][log]:
            return dp[node][log]

        if log == (1 << (n-1)) - 1:
            return path[node][st_node] if path[node][st_node] else INF
            
        min_dist = INF
        for i in range(1, n):
            if log & (1 << (i-1)) \
                    or not path[node][i]:
                continue
            
            min_dist = min(min_dist, \
                           path[node][i] + dfs(i, log | (1 << (i-1))))
        
        dp[node][log] = min_dist
        return min_dist
    return dfs(st_node, 0)


n = int(input())
path = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, path))