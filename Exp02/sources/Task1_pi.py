import math
from decimal import Decimal as dec, getcontext
import sympy


def solution1():  # 使用math模块计算
    print("Using math module:")
    print(f"pi={math.pi}")
    coef = 2 * math.sqrt(2) / 9801  # 系数
    term_sum = 0
    k = 0
    while True:
        term_sum += math.factorial(4 * k) * (1103 + 26390 * k)\
                    / (math.factorial(k) ** 4) / (396 ** (4 * k))  # 计算级数前k项和
        cal_pi = 1 / (coef * term_sum)  # 计算本次迭代所得pi值
        diff = cal_pi - math.pi
        print(f"k={k}: cal_pi={cal_pi:.15f}, difference={diff}")
        if diff < 3e-16:  # 当误差小于3e-16时停止迭代
            break
        k += 1


def solution1_better():  # 借助decimal对象计算
    print("\nUsing decimal module:")
    print(f"pi={math.pi}")
    getcontext().prec = 30  # 设置decimal对象的精度
    coef = dec(2) * dec(2).sqrt() / dec(9801)  # 系数
    term_sum = dec(0)
    k = 0
    while True:
        a = dec(math.factorial(4*k))
        b = dec(1103 + 26390 * k)
        c = dec(math.factorial(k) ** 4)
        d = dec(396 ** (4 * k))
        term_sum += a * b / c / d  # 计算级数前k项和
        cal_pi = dec(1) / (coef * term_sum)  # 计算本次迭代所得pi值
        diff = abs(dec(math.pi) - cal_pi)
        print(f"k={k}: cal_pi={cal_pi:.15f}, difference={diff}")
        if diff < dec(3e-16):  # 当绝对误差小于3e-16时停止迭代
            break
        k += 1


def solution2():  # 使用sympy模块计算
    print("\nUsing sympy module:")
    k = sympy.Symbol("k")  # 定义符号k
    func = sympy.factorial(4 * k) * (1103 + 26390 * k) / (sympy.factorial(k) ** 4) / (396 ** (4 * k))
    term_sum = sympy.summation(func, (k, 0, sympy.oo))  # 直接计算无穷级数
    coef = 2 * sympy.sqrt(2) / 9801  # 系数
    cal_pi = 1 / (coef * term_sum)
    print(f"pi={sympy.pi.evalf(16)}")
    print(f"cal_pi={cal_pi.evalf(18)}, difference={abs(sympy.pi - cal_pi).evalf()}")


solution1()
solution1_better()
solution2()
