import datetime


def solution1():  # 一般解法
    s = input("Please enter a time (hh:mm:ss, 24-hour clock): ")
    while True:
        try:
            # 按字符':'划分，划分失败将抛出ValueError异常
            hour, minute, second = map(int, s.split(':'))
            # 若数值不合法，则手动抛出ValueError异常
            if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
                raise ValueError
            break  # 无异常
        # 捕获异常，要求用户重新输入
        except ValueError:
            s = input("Input error! Please enter the time (hh:mm:ss, 24-hour clock): ")

    second += 1
    if second == 60:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0
    print(f"\nOne second later, it is {hour:02}:{minute:02}:{second:02}.")


def solution2():  # 使用datetime模块
    s = input("Please enter a time (hh:mm:ss, 24-hour clock): ")
    while True:
        try:
            # 若数值不合法，则抛出ValueError异常
            time = datetime.datetime.strptime(s, "%H:%M:%S")
            break
        # 捕获异常，要求用户重新输入
        except ValueError:
            s = input("Input error! Please enter the time (hh:mm:ss, 24-hour clock): ")

    time += datetime.timedelta(seconds=1)  # 加1秒
    print("\nOne second later, it is {}.".format(time.strftime("%H:%M:%S")))


if __name__ == '__main__':
    # solution1()
    solution2()