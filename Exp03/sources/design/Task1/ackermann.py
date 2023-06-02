import sys
sys.setrecursionlimit(1000)


"""
Ack(0, n) = n+1
Ack(1, n) = n+2 = 2 + (n+3) - 3
Ack(2, n) = 2n + 3 = 2 * (n+3) - 3
Ack(3, n) = 2 ^ (n+3) - 3 = 2 ↑ (n+3) - 3 （高德纳箭号表示法）
Ack(4, n) = 2 ↑↑ (n+3) - 3 （幂塔）
...
Ack(m, n) = (2 -> (n+3) -> (m-2)) - 3 = 2 ↑^(m-2) (n+3)-3 （康威链式箭号表示法）
"""


def Ack1(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ack1(m-1, 1)
    elif m > 0 and n > 0:
        return Ack1(m-1, Ack1(m, n-1))
    raise ValueError("Illegal parameter!")


def Ack2(m: int, n: int) -> int:
    while m > 0:
        if n == 0:
            n = 1
        else:
            n = Ack2(m, n-1)
        m = m - 1
    return n + 1


for M in range(6):
    for N in range(6):
        try:
            print(f"Ack1({M}, {N}) = {Ack1(M, N)}")
        except RecursionError:
            print(f"Ack1({M}, {N}) = 无法计算")
        try:
            print(f"Ack2({M}, {N}) = {Ack2(M, N)}\n")
        except RecursionError:
            print(f"Ack2({M}, {N}) = 无法计算\n")
