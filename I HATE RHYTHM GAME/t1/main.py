import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 設定遊戲視窗大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("O2Jam-like Game")

# 定義顏色
white = (255, 255, 255)
black = (0, 0, 0)

# 設定按鍵的位置
key_positions = [100, 200, 300, 400]

# 設定按鍵的顏色
key_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# 載入音樂
pygame.mixer.music.load("your_music_file.mp3")

# 設定時鐘
clock = pygame.time.Clock()

# 定義按鍵物件
class Key(pygame.sprite.Sprite):
    def __init__(self, position, color):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = position
        self.rect.y = 500  # 按鍵的初始 y 座標

# 創建按鍵群組
all_keys = pygame.sprite.Group()

# 加入按鍵到群組
for i in range(4):
    key = Key(key_positions[i], key_colors[i])
    all_keys.add(key)

# 開始遊戲迴圈
pygame.mixer.music.play(-1)  # 循環播放音樂
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新遊戲邏輯

    # 清空畫面
    screen.fill(white)

    # 繪製按鍵
    all_keys.draw(screen)

    # 更新顯示
    pygame.display.flip()

    # 控制遊戲迴圈更新速度
    clock.tick(60)
