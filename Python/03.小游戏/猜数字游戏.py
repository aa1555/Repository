import random

number_to_guess = random.randint(1, 100)
guess = None
guess_count = 0  # 初始化猜次数计数器

while guess != number_to_guess:
    guess = input("猜一个1到100之间的数字：")
    guess = int(guess)
    guess_count += 1  # 每次循环猜次数加一
    if guess < number_to_guess:
        print("太小了！")
    elif guess > number_to_guess:
        print("太大了！")
    else:
        print(f"恭喜你，猜对了！你总共猜了{guess_count}次。")