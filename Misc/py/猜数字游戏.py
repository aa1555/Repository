import random

number_to_guess = random.randint(1, 100)
guess = None

while guess != number_to_guess:
    guess = input("猜一个1到100之间的数字：")
    guess = int(guess)
    if guess < number_to_guess:
        print("太小了！")
    elif guess > number_to_guess:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")