"""
说明：
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
"""
from random import randint   # 从random模块中导入randint函数
money = 1000
while money > 0:    # 只要money大于0，就可以一直玩下去。每一局都要判断一次，每一局分出胜负都从这开始，满足条件就继续，不满足条件就直接到底部输出破产
    print(f'你的总资产为: {money}元')
    go_on = False  
    while True:   # 用来控制下注金额，下注金额必须大于0小于等于玩家总资产
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break # 下注金额在规定范围内，循环停止，游戏继续
    # 第一次摇色子，每一局的第一次
    first = randint(1, 6) + randint(1, 6)      # 用1到6均匀分布的随机数模拟摇色子得到的点数
    print(f'\n玩家摇出了{first}点')
    if first == 7 or first == 11:
        print('玩家胜!\n')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!\n')
        money -= debt
    else:   
        go_on = True  # 第一次摇色子没有分出胜负，游戏继续，go_on是用来控制循环的。

    while go_on:   
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜!\n')
            money -= debt
        elif current == first:
            print('玩家胜!\n')
            money += debt
        else:
            go_on = True
print('你破产了, 游戏结束!')