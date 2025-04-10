def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "除数不能为0"

operations = {
    "add": ("加法", add),
    "subtract": ("减法", subtract),
    "multiply": ("乘法", multiply),
    "divide": ("除法", divide),
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("请输入一个有效的数字。")

while True:
    print("选项：")
    for key, (name, _) in operations.items():
        print(f"输入 '{key}' 进行{name}")
    print("输入 'quit' 退出程序")
    
    user_input = input(": ").strip().lower()

    if user_input == "quit":
        print("程序已退出。")
        break

    if user_input in operations:
        x = get_number("输入第一个数字: ")
        y = get_number("输入第二个数字: ")
        result = operations[user_input][1](x, y)
        print(f"结果: {result}")
    else:
        print("无效输入，请重试。")