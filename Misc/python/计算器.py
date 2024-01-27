def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "除数不能为0"

while True:
    print("选项：")
    print("输入 'add' 进行加法")
    print("输入 'subtract' 进行减法")
    print("输入 'multiply' 进行乘法")
    print("输入 'divide' 进行除法")
    print("输入 'quit' 退出程序")
    user_input = input(": ")

    if user_input == "quit":
        break

    elif user_input in ("add", "subtract", "multiply", "divide"):
        x = float(input("输入第一个数字: "))
        y = float(input("输入第二个数字: "))

        if user_input == "add":
            print(add(x, y))
        elif user_input == "subtract":
            print(subtract(x, y))
        elif user_input == "multiply":
            print(multiply(x, y))
        elif user_input == "divide":
            print(divide(x, y))
    else:
        print("无效输入")