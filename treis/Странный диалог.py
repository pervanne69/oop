n = int(input())

l = [input() for _ in range(n)]
for i in range(n):
    a = l[i]
    if "puton" in a and a.index("puton") + 5 >= len(a):
        a = a.replace("puton", "")
    elif "puton" in a and a.index("puton") + 5 < len(a) and a[a.index("puton") + 5] != 'e':
        a = a.replace("puton", "")
    if "one" in a:
        a = a.replace("one", "")
    if "output" in a:
        a = a.replace("output", "")
    if "out" in a:
        a = a.replace('out', "")
    if "input" in a:
        a = a.replace("input", "")
    if "in" in a:
        a = a.replace("in", "")
    if not a:
        print('YES')
    else:
        print("NO")