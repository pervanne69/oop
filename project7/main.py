n = int(input())

grades = [int(input()) for _ in range(n)]
total = sum(grades)
if grades.count(3) >= 1:
    print("None")
elif total / n == 5.0:
    print("Named")
elif float(total / n) >= 4.5:
    print("High")
else:
    print("Common")
