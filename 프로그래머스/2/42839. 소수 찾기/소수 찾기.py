"""
순열을 다 생성 해야 한다.
그리고 int로 형변환 해서 앞에 있는 0을 나려 먹는다.
그리고 이게 소수인지 판별한다.
소수 판별시에는 효율을 위해 에라토스 테네스의 체를 활용한다.
조합으로 생성된 가장 큰 수로 테네스의 체의 크기를 결정한다
"""

def eratos(max_num):
    field = [True] * (max_num+1)
    field[0] = field[1] = False
    
    for i in range(2, int(max_num**0.5)+1):
        for j in range(i*2, len(field), i):
            field[j] = False
    return field
            
def solution(numbers):
    def combination(idx, cnt):
        nonlocal tmp
        
        if cnt == 0:
            result.add(int(tmp))
            return
        
        for i in range(len(numbers)):
            if i in picked_idx:
                continue
                
            tmp += numbers[i]
            picked_idx.append(i)
            
            combination(idx+1, cnt-1)
            
            tmp = tmp[:-1]
            picked_idx.pop()
    
    result = set()
    picked_idx = []
    tmp = ""
    
    for i in range(1, len(numbers)+1):
        combination(0, i)
    
    eratos_field = eratos(max(result)) 
    
    return sum([eratos_field[i] for i in result])