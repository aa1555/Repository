def adventure_game():
    print("你醒来发现自己在一个神秘的森林里。")
    choice = input("你想要往左边走还是右边走？（输入'left'或'right'）")

    if choice.lower() == 'left':
        print("你发现了一条小溪和一只友好的兔子。")
    elif choice.lower() == 'right':
        print("你遇到了一只熊，看起来它很饿...")
    else:
        print("你犹豫不决，被困在了森林里。")

adventure_game()
