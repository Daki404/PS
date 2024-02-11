import sys; input = sys.stdin.readline


n, x = map(int, input().split())
line = list(map(int, input().split()))


max_visit = sum(line[:x])
tmp_visit = max_visit
count = 1

for i in range(1, n-x+1):
    tmp_visit -= line[i-1]
    tmp_visit += line[i+x-1]

    if tmp_visit > max_visit:
        max_visit = tmp_visit
        count = 1
    
    elif tmp_visit == max_visit:
        count += 1

if max_visit > 0:
    print(max_visit)
    print(count)
else:
    print('SAD')