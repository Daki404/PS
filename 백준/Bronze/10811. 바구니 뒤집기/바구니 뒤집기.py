n, m = map(int, input().split())
busket = list(range(1, n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    
    for i in range(((b-a) // 2) + 1):
        busket[a+i], busket[b-i] = busket[b-i], busket[a+i] 
        
print(*busket)