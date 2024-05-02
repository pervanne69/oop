from math import gcd


def main() -> None:
    """
    This is the main function and entry point of program
    :return:
    """
    p, q = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    dx = x2 - x1
    dy = y2 - y1
    g = gcd(p, q)

    if not dx and not dy:
        print("YES")
        return
    if not p and not q or dx % g or dy % g:
        print("NO")
        return

    dx //= g
    dy //= g
    p //= g
    q //= g

    print("YES" if (p & 1 ^ q & 1 or not ((dx + dy) & 1)) else "NO")


if __name__ == "__main__":
    main()
