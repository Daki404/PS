import sys
input = sys.stdin.readline

num, k_len = map(int, input().split())
k = list(map(int, input().split()))


def sol(arr, n):
    def permuatation(arr, n):
        for i in range(len(arr)):
            if n == 1:
                yield str(arr[i])
            else:
                for next in permuatation(arr, n - 1):
                    yield str(arr[i]) + next

    for i in range(len(str(num)), 0, -1):
        possible = sorted(permuatation(k, i), reverse=True)
        for i in possible:
            if int(i) <= num: return i


print(sol(k, len(str(num))))