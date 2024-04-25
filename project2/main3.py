t = int(input())

l = [int(input()) for _ in range(t)]

for i in range(t):
    count_of_d = 0
    count_of_odd = 0
    current = l[i]
    if current == 1:
        print("NO")
        continue
    while current % 2 == 0:
        current //= 2
        count_of_d += 1
    if current == 1:
        if count_of_d % 2 == 0:
            print("NO")
        else:
            print("YES")
    else:
        j = 3
        while current != 1:
            if current % j == 0:
                count_of_odd += 1
                if j != current // j and (current // j) != 1:
                    count_of_odd += 1
                    current //= j
                    current //= current
                else:
                    current //= j
            else:
                j += 2
        if count_of_odd == 1:
            total = count_of_d + count_of_odd
            if total % 2 == 0:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")