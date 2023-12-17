import sys

input = sys.stdin.readline

n, l = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for h in range(n):
    streak = 0
    resolve = False
    height = field[h][0]
    
    for w in range(n):
        if (new_height := field[h][w]) == height:
            streak += 1
            
            if streak >= l\
                    and resolve:
                resolve = False
                streak = 0
        
        elif resolve:
            break

        else:
            diff_height = new_height - height
            
            # 높아질 때
            if diff_height == 1:
                if streak < l:
                    break
            # 낮아질 때
            elif diff_height == -1:
                resolve = True
            # 높이가 2이상 변할 때
            else:
                break
            
            if resolve\
                    and l == 1:
                streak = 0
                resolve = False
            else:
                streak = 1
            height = new_height

    else:
        if not resolve:
            ans += 1


for w in range(n):
    streak = 0
    resolve = False
    height = field[0][w]
    
    for h in range(n):
        if (new_height := field[h][w]) == height:
            streak += 1
            
            if streak >= l\
                    and resolve:
                resolve = False
                streak = 0
        
        elif resolve:
            break

        else:
            diff_height = new_height - height
            
            # 높아질 때
            if diff_height == 1:
                if streak < l:
                    break
            # 낮아질 때
            elif diff_height == -1:
                resolve = True
            # 높이가 2이상 변할 때
            else:
                break

            if resolve\
                    and l == 1:
                streak = 0
                resolve = False
            else:
                streak = 1
            height = new_height
    else:
        if not resolve:
            ans += 1

print(ans)