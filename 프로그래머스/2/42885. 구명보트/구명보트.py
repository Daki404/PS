def solution(people, limit):
    people.sort()
    
    cobi_cnt = 0
    st, ed = 0, len(people) -1
    
    while st < ed:
        if people[st] + people[ed] <= limit:
            cobi_cnt += 1
            st += 1
            ed -= 1
        else:
            ed -= 1
    
    return len(people) - cobi_cnt