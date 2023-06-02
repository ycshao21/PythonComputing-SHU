import Food


class Employee:
    def takeOrder(self):
        foodName = input("请输入您想要点的菜品：")
        foodName = foodName.strip()
        while foodName == "":  # 无效输入
            foodName = input("输入有误，请重新输入您想要点的菜品：")

        num = input("请输入份数：")
        try:
            num = int(num)
            if num < 1:
                raise ValueError
        except ValueError:
            num = input("输入有误，请重新输入份数：")
        return Food.Food(foodName, num)

    def removeDish(self):
        foodName = input("请输入您想要取消的菜品：")
        foodName = foodName.strip()
        while foodName == "":  # 无效输入
            foodName = input("输入有误，请重新输入您想要取消的菜品：")
        return Food.Food(foodName)

