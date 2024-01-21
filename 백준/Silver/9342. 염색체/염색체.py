import re

p = re.compile("^[A-F]{0,1}A+F+C+[A-F]{0,1}$")
n = int(input())

for _ in range(n):
    result = p.match(input().strip())

    if result is None:
        print("Good")
    else:
        print("Infected!")