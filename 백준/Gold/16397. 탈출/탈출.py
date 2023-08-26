import sys
from collections import deque

input = sys.stdin.readline


def get_min_press(n: int, t: int, g: int) -> int | str:
    def press_a(a: int) -> int:
        return a + 1
    
    def press_b(a: int) -> int:
        a *= 2
        
        if a >= 100000:
            return 100000
        
        for i in range(4, -1, -1):
            if 10 ** i <= a:
                a -= 10 ** i
                break

        return a

    def bfs(x: int, depth: int) -> int:    
        dp = {}
        queue = deque([(x, depth)])

        while queue:
            x, depth = queue.popleft()
            
            if x == g:
                return depth

            if dp.get(x) is None:
                dp[x] = depth
            else:
                continue
            
            if depth < t:
                pressed_a = press_a(x)
                pressed_b = press_b(x)

                if pressed_a < 100000:
                    queue.append((press_a(x), depth + 1))
                if pressed_b < 100000:
                    queue.append((press_b(x), depth + 1))
        
        return dp.get(g, "ANG")

    return bfs(n, 0)

N, T, G = map(int, input().split())
print(get_min_press(N, T, G))