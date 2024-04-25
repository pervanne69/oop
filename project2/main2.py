t = int(input())

l = [int(input()) for i in range(t)]
k = 0
count = 0
for i in range(t):
    count = 0
    current = l[k]
    if current == 1:
        print("NO")
        k += 1
        continue
    j = 3
    j_com = 0
    while j <= current or current != 1:
        if count % 2 == 0 and current % 2 != 0:
            current = 1
            count += 1
            j_com = 2
        else:
            if current % j == 0:
                current //= j
                count += 1
                j_com += 1
            elif current % 2 == 0:
                current //= 2
                count += 1
            else:
                j += 2
            if current != 1:
                if j_com == 2:
                    if count % 2 == 0:
                        count -= 1
                    j_com -= 1

    if j_com == 2 and count % 2 == 0:
        count -= 1
    if current == 1:
        if count % 2 != 0:
            print("YES")
        else:
            print("NO")
    else:
        print('NO')
    k += 1
