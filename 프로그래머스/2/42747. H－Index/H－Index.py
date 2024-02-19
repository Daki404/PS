def solution(citations):
    citations.sort()
    ret = 0
    
    for i in range(len(citations)-1, -1, -1):
        if (len(citations) - i) <= citations[i]:
            ret = max(ret, (len(citations) - i))
    return ret
        