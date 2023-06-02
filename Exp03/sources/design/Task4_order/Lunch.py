import Customer
import Employee


class Lunch:
    def __init__(self):
        self.customer = Customer.Customer()  # 顾客
        self.employee = Employee.Employee()  # 员工
        self.foodDict = dict()  # 订单

    def order(self):  # 点单
        food = self.customer.placeOrder(self.employee)
        self.foodDict[food.name] = self.foodDict.get(food.name, 0) + food.num
        print("菜品添加成功！")

    def remove(self):
        food = self.customer.removeDish(self.employee)
        if food.name in self.foodDict:
            self.foodDict.pop(food.name)
            print("已取消该菜品！")
        else:
            print("订单中无该菜品！")

    def result(self):  # 显示订单
        if len(self.foodDict) == 0:
            print("订单空空的哦~")
        for foodName, foodNum in self.foodDict.items():
            print(f"{foodName} × {foodNum}")
