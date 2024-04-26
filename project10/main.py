L, T, va, vb = map(int, input().split())
n = int(input())
t = [0, 0]

for _ in range(n):
    i, tmp, d = map(int, input().split())
    t[i - 1] += d

print(int((va * (T - t[0]) + vb * (T - t[1])) / L))
