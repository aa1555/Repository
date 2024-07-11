def chat_bot():
    print("你好，我是聊天机器人。输入'quit'结束聊天。")
    while True:
        user_input = input("你：")
        if user_input.lower() == 'quit':
            print("机器人：再见！")
            break
        else:
            print(f"机器人：{user_input}，你再说一遍？")

chat_bot()