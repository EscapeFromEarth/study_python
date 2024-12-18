import pygame
import sys
import time

color1 = (0, 128, 128)
color2 = (50, 50, 50)
color3 = (255, 0, 0)

pygame.init()

screen_image = pygame.display.set_mode((800, 600))
screen_rect = screen_image.get_rect()
pygame.display.set_caption('test')

small_head = pygame.image.load('imgs/yelaoji.png')
small_head_rect = small_head.get_rect()
small_head_rect.center = screen_rect.center

# 这里的 Rect 的 R 要用大写！(50, 100) 表示坐标，(20, 50) 表示宽高
bullet_rect = pygame.Rect(50, 100, 8, 20)
bullet_rect.midbottom = small_head_rect.midtop

text_font = pygame.font.SysFont(None, 48)
text_image = text_font.render('TEST', True, color2, color3)
text_rect = text_image.get_rect()
text_rect.x = 680
text_rect.y = 30

def display():
	screen_image.fill(color1)
	screen_image.blit(text_image, text_rect)
	screen_image.blit(small_head, small_head_rect)
	pygame.draw.rect(screen_image, color2, bullet_rect)
	pygame.display.flip()

display()

while True:
	for event in pygame.event.get():
		# 这个 QUIT 还必须是大写的，小写的没用
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				small_head_rect.x -= 10
			if event.key == pygame.K_RIGHT:
				small_head_rect.x += 10
			if event.key == pygame.K_UP:
				small_head_rect.y -= 10
			if event.key == pygame.K_DOWN:
				small_head_rect.y += 10
	
	bullet_rect.y -= 1
	display()
	time.sleep(0.01)