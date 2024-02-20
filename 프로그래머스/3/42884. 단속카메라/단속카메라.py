def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]), reverse=True)
    
    ret = 0
    while routes:
        ret += 1
        st, ed = routes.pop()
        
        while routes\
                and routes[-1][0] <= ed:
            routes.pop()
    
    return ret