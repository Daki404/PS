import sys

input = sys.stdin.readline

def analyze_signal(signal: str) -> str:
    stack = list(signal)

    while len(stack) >= 2 \
            and stack[-1] == "1":
        if stack[-2:] == ["0", "1"] \
                and (len(stack) == 2 \
                or stack[-3:] == ["1", "0", "1"]):
            stack.pop()
            stack.pop()
        
        else:
            flag = [False, True]
            zero_cnt = 0
            state = None

            while stack:
                if all(flag):
                    break

                now = int(stack.pop())
                zero_cnt += now == 0

                if state != now:
                    flag[now] = not flag[now]
                    state = now
            else:
                return "YES" if all(flag) and zero_cnt >= 2 else "NO"
            
            if zero_cnt < 2:
                return "NO"

    return "NO" if stack else "YES"
   

n = int(input())

for _ in range(n):
    signal = input().strip()
    print(analyze_signal(signal))