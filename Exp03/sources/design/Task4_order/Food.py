class Food:  # 食物类
    def __init__(self, foodName, num=0):
        self.name = foodName  # 名称
        self.num = num  # 份数

    def __str__(self):
        return self.name

    __repr__ = __str__
