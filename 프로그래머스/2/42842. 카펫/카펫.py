"""
갈색은 노랑 보다 가로 2 세로 2가 더 길다.
노랑 = (x, y)라 할 때, 갈색 = (x+2, y+2)이다.
x*y 와 (2x + 2y + 4)가 주어질 때 x와 y를 구해라.
x*y, 2(x+y)+4


"""

def solution(brown, yellow):
    x_plus_y = (brown+4)//2
    x_dot_y = yellow + 2*x_plus_y -4
    
    for x in range(3, x_dot_y+1):
        if (y:= (x_dot_y / x)) == (x_plus_y - x):
            return (max(y,x), min(y, x))