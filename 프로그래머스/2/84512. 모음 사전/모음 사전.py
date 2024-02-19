"""
이분 탐색으로 찾고 싶다.
대소 비교가 가능 해야 함.
1 11 111 1111 11111 11112 11113 11114 11115 111120
55550 55555

"""
def solution(word):
    def get_length(num):
        cnt = 0
        while num:
            num = num // 10
            cnt += 1
        
        return cnt
    
    alpha_mapper = {val:str(idx+1) for idx, val in enumerate('AEIOU')}
    num_word = ['0'] * 5
    
    for idx, val in enumerate(word):
        num_word[idx] = alpha_mapper[val]
    
    num_word = int(''.join(num_word))
    
    cnt = 0
    for i in range(10000, num_word+1):
        str_i = str(i)
        
        if '0' in str_i.rstrip('0'):
            continue
        
        for j in str_i:
            if int(j) > 5:
                break
        else:
            cnt += 1
    
    return cnt
    
    
    

    