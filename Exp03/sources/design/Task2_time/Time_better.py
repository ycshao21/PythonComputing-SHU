class Time:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        if not (isinstance(hour, int) and isinstance(minute, int) and isinstance(second, int)):
            raise TypeError("hour, minute and second must be integer.")
        if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
            raise ValueError("hour, minute and second must be in range 0~23, 0~59 and 0~59.")
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self) -> str:
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

    __repr__ = __str__

    def __add__(self, other: "Time") -> "Time":
        # 检查参数合法性
        if isinstance(other, Time):
            raise TypeError("other must be a Time object.")
        newTime = Time(self.__hour, self.__minute, self.__second)
        newTime.increment(other.time2int())
        return newTime

    def time2int(self) -> int:
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    def print_time(self) -> None:
        print(self.__str__())

    def is_after(self, other: "Time") -> bool:
        return self.time2int() > other.time2int()

    def increment(self, seconds: int):
        # 检查参数合法性
        if not isinstance(seconds, int):
            raise TypeError("seconds must be integer.")
        if seconds <= 0:
            raise ValueError("seconds must be positive.")
        # 求时、分、秒
        rest, self.__second = divmod(self.time2int() + seconds, 60)
        self.__hour, self.__minute = divmod(rest, 60)
        self.__hour %= 24


if __name__ == '__main__':
    t1 = Time(10, 30)  # 10:30:00
    t2 = Time(11, 41, 8)  # 11:41:08
    t1.print_time()
    t2.print_time()
    print(f"t1 + t2 = {t1 + t2}")  # 22:11:08
    t3 = Time(23, 41, 12)  # 23:41:12
    print(t1.is_after(t3))

