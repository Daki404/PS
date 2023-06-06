n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = sum([i*j for i, j in zip(a, b)])
print(result)