import Lunch
import sys


def orderSystem():
    lunch = Lunch.Lunch()
    while True:
        print("亲爱的顾客，欢迎您使用本餐厅的订餐系统~")
        print("-" * 33)
        print("[1] 选择菜品")
        print("[2] 取消菜品")
        print("[3] 查看订单")
        print("[4] 退出")

        choice = input("请输入模块编号: ")
        # 读取顾客选择
        while choice.strip() not in ('1', '2', '3', '4'):
            choice = input("输入无效，请重新输入模块编号: ")

        print()
        print("-" * 35)

        # 模块跳转
        if choice == '1':  # 选择菜品
            print("[1] 选择菜品")
            lunch.order()
            print("按回车键返回主菜单...")
            sys.stdin.read(1)
        elif choice == '2':  # 取消菜品
            print("[2] 取消菜品")
            lunch.remove()
            print("按回车键返回主菜单...")
            sys.stdin.read(1)
        elif choice == '3':  # 查看订单
            print("[3] 显示订单")
            lunch.result()
            print("按回车键返回主菜单...")
            sys.stdin.read(1)
        elif choice == '4':  # 退出
            print("感谢使用本订餐系统！")
            break


orderSystem()
