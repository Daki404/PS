import sys
input = sys.stdin.readline

def sol(start):
    for i in range(1, n):
        # 높이 차 2 이상인 것 만나면 바로 컷
        if abs(start[i]-start[i-1]) >= 2:
            return 0
        if start[i] < start[i-1]:
            for k in range(l):
                if i+k >= n or check[i+k] or start[i] != start[i+k]:
                    return 0
                check[i+k] = 1
        elif start[i] > start[i-1]:
            for k in range(l):
                if i-k-1 < 0 or start[i-1] != start[i-k-1] or check[i-k-1]:
                    return 0
                check[i-k-1] = 1
    return 1

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    check = [0 for _ in range(n)]
    if sol(arr[i]):
        res += 1

for i in range(n):
    check = [0 for _ in range(n)]
    if sol([arr[j][i] for j in range(n)]):
        res += 1

print(res)