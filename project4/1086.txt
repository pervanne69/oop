n_max = 2 * 10 ** 5
a = list(range(n_max + 1))
a[1] = 0
lst = []
i = 2
while i <= n_max:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n_max + 1, i):
            a[j] = 0
    i += 1

n = int(input())
res = [0] * n
for i in range(n):
    res[i] = lst[int(input()) - 1]

print(*res, sep="\n")