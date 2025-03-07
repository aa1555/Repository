import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 使用本地字体文件
font = pygame.font.Font("msyh.ttc", 36)  # 使用本地的微软雅黑字体文件

# 游戏常量
WIDTH = 800
HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 7
ENEMY_SPEED = 3
FPS = 60

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 初始化屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("太空射击游戏")
clock = pygame.time.Clock()

# 加载图像
player_img = pygame.image.load("player.png")  # 需要准备玩家图片
enemy_img = pygame.image.load("enemy.png")    # 需要准备敌人图片
bullet_img = pygame.image.load("bullet.png")  # 需要准备子弹图片

# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT-50)
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()

# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        self.speed = ENEMY_SPEED
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

# 创建精灵组
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

score = 0
# font = pygame.font.Font(None, 36)  # 注释掉原来的字体初始化

# 生成敌人定时器
ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_EVENT, 1000)

running = True
game_over = False

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
        elif event.type == ENEMY_EVENT and not game_over:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)
    
    if not game_over:
        all_sprites.update()
        
        # 检测子弹和敌人的碰撞
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
            
        # 检测玩家和敌人的碰撞
        if pygame.sprite.spritecollide(player, enemies, True):
            game_over = True
    
    screen.fill((0, 0, 0))
    
    # 绘制所有精灵
    all_sprites.draw(screen)
    
    # 显示分数
    score_text = font.render(f"分数: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render("游戏结束 - 按'R'重新开始", True, RED)
        screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            score = 0
            for entity in all_sprites:
                entity.kill()
            player = Player()
            all_sprites.add(player)
    
    pygame.display.flip()

pygame.quit()
sys.exit()