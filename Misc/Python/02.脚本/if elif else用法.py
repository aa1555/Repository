print("请输入任意一个整数数字：")

try:
    number = int(input())  # 尝试将输入转换为整数
    print(f"您输入的数字是：{number}")

    if number == 10:
        print("You are SMART.")
    elif number > 10:
        print("This number is more than 10.")
    elif number < 10:
        print("This number is less than 10.")
except ValueError:  # 捕获非整数输入的错误
    print("输入错误，请输入一个整数。")