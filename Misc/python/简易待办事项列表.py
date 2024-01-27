todos = []

while True:
    action = input("请输入命令（添加、完成、显示或退出）：")
    if action == "添加":
        todo = input("请输入待办事项：")
        todos.append(todo)
    elif action == "完成":
        index = int(input("请输入待办事项的编号："))
        if 0 <= index < len(todos):
            completed = todos.pop(index)
            print(f"已完成：{completed}")
        else:
            print("编号无效。")
    elif action == "显示":
        for i, todo in enumerate(todos):
            print(f"{i}. {todo}")
    elif action == "退出":
        break
    else:
        print("无效的命令。")