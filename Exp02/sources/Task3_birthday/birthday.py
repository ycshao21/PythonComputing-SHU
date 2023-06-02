import random


def inputInfo(lower_bound=1000):
    s = input(f"请输入班级数M（不少于{lower_bound}）和各班的学生数N: ")
    while True:
        try:
            m, n = map(int, s.split())
            if m < lower_bound or n <= 0:
                raise ValueError
            break
        except ValueError:
            s = input(f"输入有误！请重新输入班级数M（不少于{lower_bound}）和各班的学生数N: ")
    return m, n


def count_same_birthday(m, n):
    q = 0  # 存在相同生日的班级数
    days_in_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    for i in range(m):
        cur_class = set()  # 当前班级的生日集合
        for j in range(n):
            # 随机生成一个生日
            month = random.randint(1, 12)
            day = random.randint(1, days_in_month[month-1])
            # 若生日存在于cur_class，则表明该班至少有两名同学生日相同
            if (month, day) in cur_class:
                q += 1  # 符合条件
                break
            # 否则，将新生成的生日加入cur_class
            cur_class.add((month, day))
    return q


def printResult(m, n, q):
    print(f"\n班级数M = {m}")
    print(f"各班学生数N = {n}")
    print(f"存在相同生日情况的班级数Q = {q}")
    print(f"概率估计值P = {q / m}")


if __name__ == '__main__':
    M, N = inputInfo()
    Q = count_same_birthday(M, N)
    printResult(M, N, Q)
