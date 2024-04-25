from math import sqrt
n = int(input())

res = ""

for i in range(n):
    index = int(input()) - 1
    a = round(sqrt(index * 8 + 1), 1)
    b = sqrt(index * 8 + 1)
    if a == b:
        res += '1 '
    else:
        res += '0 '
print(res)

