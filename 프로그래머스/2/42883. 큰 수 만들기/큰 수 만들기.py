def solution(number, k):
    idx = 0
    ret = []
    
    for i in number:
        while ret\
                and ret[-1] < i\
                and k > 0:
            k -= 1
            ret.pop()
        
        ret.append(i)
    
    return ''.join(ret[:len(number)-k])
                
        
        
            
        
        
    


