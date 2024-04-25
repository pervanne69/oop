from math import sqrt

l, h, w = map(int, input().split())

if l / 2 > h:
    print('butter')
else:
    g = 9.81
    w /= 60
    h /= 100
    l /= 100
    h -= l / 2
    t = sqrt(2 * h / g)
    n = w * t
    n -= int(n)

    if n <= 0.25 or n >= 0.75:
        print("butter")
    else:
        print('bread')
