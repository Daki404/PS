def solution(n, lost, reserve):
    ret = n
    
    for i in range(1, n+1):
        if i in lost\
                and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    for i in sorted(lost):
        if i-1 in reserve:
            reserve.remove(i-1)
            continue
        
        if i+1 in reserve:
            reserve.remove(i+1)
            continue
        
        ret -= 1
    
    return ret
        