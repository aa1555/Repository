import pygame
import sys
import time
import random

# 初始化 Pygame
pygame.init()

# 定义颜色
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED   = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)

# 游戏窗口参数
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('贪吃蛇')

# 控制帧率
fps_controller = pygame.time.Clock()

# 定义蛇的速度和每个格子的大小
SNAKE_SPEED = 15
SNAKE_SIZE = 20

def game_over(score):
    """游戏结束时显示 Game Over 信息和分数，并退出游戏"""
    font = pygame.font.SysFont('arial', 50)
    go_surface = font.render('Game Over!', True, RED)
    go_rect = go_surface.get_rect()
    go_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
    
    # 显示分数
    score_font = pygame.font.SysFont('arial', 20)
    score_surface = score_font.render('Score: ' + str(score), True, WHITE)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    
    game_window.fill(BLACK)
    game_window.blit(go_surface, go_rect)
    game_window.blit(score_surface, score_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def main():
    # 初始化蛇的位置和身体（初始3节）
    snake_pos = [100, 50]
    snake_body = [
        [100, 50],
        [80, 50],
        [60, 50]
    ]

    # 初始化食物的位置（随机生成，位置为网格倍数）
    food_pos = [
        random.randrange(1, WINDOW_WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
        random.randrange(1, WINDOW_HEIGHT // SNAKE_SIZE) * SNAKE_SIZE
    ]
    food_spawn = True

    # 初始移动方向（向右）
    direction = 'RIGHT'
    change_to = direction

    score = 0  # 初始分数

    # 主游戏循环
    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 键盘事件：改变方向
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # 防止蛇直接反向移动
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # 根据方向更新蛇头的位置
        if direction == 'UP':
            snake_pos[1] -= SNAKE_SIZE
        elif direction == 'DOWN':
            snake_pos[1] += SNAKE_SIZE
        elif direction == 'LEFT':
            snake_pos[0] -= SNAKE_SIZE
        elif direction == 'RIGHT':
            snake_pos[0] += SNAKE_SIZE

        # 将新蛇头插入蛇身列表中
        snake_body.insert(0, list(snake_pos))

        # 检查是否吃到食物
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            # 未吃到食物则移除蛇尾（实现移动效果）
            snake_body.pop()

        # 如果食物已被吃掉，则生成新的食物
        if not food_spawn:
            food_pos = [
                random.randrange(1, WINDOW_WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
                random.randrange(1, WINDOW_HEIGHT // SNAKE_SIZE) * SNAKE_SIZE
            ]
            food_spawn = True

        # 填充背景
        game_window.fill(BLACK)

        # 绘制蛇：遍历每个蛇块
        for pos in snake_body:
            pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

        # 绘制食物
        pygame.draw.rect(game_window, RED, pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))

        # 检查是否撞墙（游戏结束条件之一）
        if (snake_pos[0] < 0 or snake_pos[0] > WINDOW_WIDTH - SNAKE_SIZE or
            snake_pos[1] < 0 or snake_pos[1] > WINDOW_HEIGHT - SNAKE_SIZE):
            game_over(score)

        # 检查是否撞到自身（游戏结束条件之二）
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over(score)

        # 显示分数
        font = pygame.font.SysFont('arial', 20)
        score_surface = font.render('Score: ' + str(score), True, WHITE)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (WINDOW_WIDTH / 2, 10)
        game_window.blit(score_surface, score_rect)

        # 更新显示
        pygame.display.update()

        # 控制游戏速度
        fps_controller.tick(SNAKE_SPEED)

if __name__ == '__main__':
    main()



# 游戏玩法

# 使用键盘方向键（↑、↓、←、→）控制蛇的移动方向。
# 每吃到一个食物，蛇的长度会增加，分数也会增加。
# 撞到窗口边界或自身，游戏结束并显示分数。