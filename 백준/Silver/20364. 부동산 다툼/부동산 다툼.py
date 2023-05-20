import sys

input = sys.stdin.readline


def check_field(n: int, earth: int) -> None:
    def recursive(idx: int) -> None:
        if idx > earth:
            return

        field[idx] = n
        recursive(idx * 2)
        recursive(idx*2 + 1)
    
    recursive(n)


earth, duck = map(int, input().split())
field = [None] * (earth + 1)


for _ in range(duck):
    n = int(input())

    if field[n] is not None:
        print(field[n])
        continue
    
    field[n] = n
    check_field(n, earth)
    print(0)