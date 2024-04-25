from math import ceil
a, b = map(int, input().split())

if a <= b:
    print(2)
else:
    print(ceil(a / b + 1))