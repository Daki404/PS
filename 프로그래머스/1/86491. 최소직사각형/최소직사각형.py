def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort()
    
    return (max(sizes, key=lambda x: x[0])[0] * max(sizes, key=lambda x: x[1])[1])
        