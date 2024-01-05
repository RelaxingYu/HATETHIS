import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 設定遊戲視窗大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fruit Catcher Game")

# 定義顏色
white = (255, 255, 255)
black = (0, 0, 0)

# 載入圖片
basket_image = pygame.image.load("basket.png")
fruit_images = [
    pygame.image.load("apple.png"),
    pygame.image.load("banana.png"),
    pygame.image.load("orange.png"),
]

# 設定時鐘
clock = pygame.time.Clock()

# 定義水果物件
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(fruit_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = 0  # 水果的初始 y 座標

    def update(self):
        self.rect.y += 5  # 控制水果的下降速度

# 定義籃子物件
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = basket_image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2 - self.rect.width // 2
        self.rect.y = screen_height - self.rect.height - 20

# 創建水果和籃子群組
all_sprites = pygame.sprite.Group()
fruits_group = pygame.sprite.Group()
basket_group = pygame.sprite.Group()

# 加入籃子到群組
basket = Basket()
all_sprites.add(basket)
basket_group.add(basket)

# 開始遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新遊戲邏輯

    # 產生新的水果
    if random.random() < 0.02:
        new_fruit = Fruit()
        all_sprites.add(new_fruit)
        fruits_group.add(new_fruit)

    # 更新水果位置
    fruits_group.update()

    # 清空畫面
    screen.fill(white)

    # 繪製所有物件
    all_sprites.draw(screen)

    # 檢查水果是否被籃子接住
    caught_fruits = pygame.sprite.spritecollide(basket, fruits_group, True)
    
    # 更新顯示
    pygame.display.flip()

    # 控制遊戲迴圈更新速度
    clock.tick(60)
