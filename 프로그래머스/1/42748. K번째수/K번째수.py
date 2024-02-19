def solution(array, commands):
    ret = []
    
    for st, ed, pick in commands:
        ret.append(sorted(array[st-1:ed])[pick-1])   
    
    return ret