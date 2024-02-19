from functools import cmp_to_key

def solution(numbers):
    def compare(a, b):
        t1 = int(a+b)
        t2 = int(b+a)
        
        return (t1 > t2) - (t1 < t2)
    
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=cmp_to_key(compare))
    
    return str(int(''.join(numbers)))