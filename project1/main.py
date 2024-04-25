def get_numeral(count: int) -> str:
    res = ''
    if 1 <= count <= 4:
        res = "few"
    elif 5 <= count <= 9:
        res = "several"
    elif 10 <= count <= 19:
        res = "pack"
    elif 20 <= count <= 49:
        res = "lots"
    elif 50 <= count <= 99:
        res = "horde"
    elif 100 <= count <= 249:
        res = "throng"
    elif 250 <= count <= 499:
        res = "swarm"
    elif 500 <= count <= 999:
        res = "zounds"
    else:
        res = "legion"
    return res


a = int(input())

result = get_numeral(a)

print(result)
