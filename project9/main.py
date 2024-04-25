import math

xc, yc, r = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

x_m_c = x1 - xc
y_m_c = y1 - yc

if 4 * (x_m_c ** 2 + y_m_c ** 2 - r ** 2) <= (x2 - x1) ** 2 + (y2 - y1) ** 2:
    print("No way")
else:
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2
    MO = math.sqrt((xm - xc) ** 2 + (ym - yc) ** 2)
    MS = MO - r
    Xmo = xc - xm
    Ymo = yc - ym
    Xms = MS * Xmo / MO
    Yms = MS * Ymo / MO
    xs = xm + Xms
    ys = ym + Yms
    print(f"{xs:.6f} {ys:.6f}")
