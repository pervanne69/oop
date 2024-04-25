lst = list(map(int, input().split()))
worst = sum(lst)
best = worst
last = len(lst) - 1

for index, i in enumerate(lst):
    if index != last:
        if i == 10:
            best += min(10, lst[index + 1])
            if lst[index + 1] >= 10:
                if index + 2 < last:
                    best += lst[index + 2]

                elif index + 2 == last:
                    best += min(10, lst[last])

                else:
                    best += max(0, min(10, lst[last] - 10))
                    if lst[last] > 20:
                        worst += 10

print(worst, best)