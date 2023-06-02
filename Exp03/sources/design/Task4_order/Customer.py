class Customer:  # 顾客类
    def placeOrder(self, employee):
        return employee.takeOrder()

    def removeDish(self, employee):
        return employee.removeDish()
