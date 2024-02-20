from collections import deque

def solution(name):
    def min_horizon_spin():
        fix_bit = 0
        for idx, val in enumerate(name):
            if val != 'A':
                fix_bit |= (1<<idx)
    
        queue = deque([(0, 1, 0)])
        while queue:
            now, visit, cnt = queue.popleft()
            
            if (fix_bit & visit) == fix_bit:
                return cnt
            
            r = (now+1)%len(name)
            l = (now-1+len(name))%len(name)
            queue.append((r, visit|(1<<r), cnt+1))
            queue.append((l, visit|(1<<l), cnt+1))
        
    def min_vertical_spin(st, aim):
        st, aim = min(st, aim), max(st, aim)
        distance = ord(aim) - ord(st)
        return min(distance, ord('z')-ord('a')-distance+1)
    
    ret = sum(min_vertical_spin('A', i) for i in name)
    ret += min_horizon_spin()
    
    return ret
    
    
        
        
        