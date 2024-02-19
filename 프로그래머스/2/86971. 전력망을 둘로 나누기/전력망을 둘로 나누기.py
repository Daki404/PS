"""
전선을 하나씩 다 끊어 본다.
그리고 SUM DFS를 때리고 차를 구하고,
차가 최소가 되는 값을 구한다
"""

def diff_elect(n, road):
    def dfs(i):
        stack = [i]
        visit[i] = True
        
        while stack:
            node = stack.pop()
            
            for idx, is_road in enumerate(road[node]):
                if not is_road\
                        or visit[idx]:
                    continue
                
                stack.append(idx)
                visit[idx] = True
        
        return sum(visit)
        
    visit = [False] * (n+1)
    return abs(n - 2*dfs(1))
    
    
def solution(n, wires):
    ret = float('inf')
    road = [[False] * (n+1) for _ in range(n+1)]
    
    for st, ed in wires:
        road[st][ed] = True
        road[ed][st] = True
    
    for cut in range(len(wires)):
        st, ed = wires[cut]
        
        road[st][ed] = False
        road[ed][st] = False
        
        ret = min(ret, diff_elect(n, road))
        
        road[st][ed] = True
        road[ed][st] = True
    
    return ret
    