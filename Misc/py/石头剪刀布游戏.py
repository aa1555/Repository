import random

choices = ["石头", "剪刀", "布"]
computer = random.choice(choices)
player = input("请选择石头、剪刀或布：")

print(f"电脑选择了：{computer}")
print(f"你选择了：{player}")

if player == computer:
    print("平局！")
elif (player == "石头" and computer == "剪刀") or (player == "剪刀" and computer == "布") or (player == "布" and computer == "石头"):
    print("你赢了！")
else:
    print("你输了！")