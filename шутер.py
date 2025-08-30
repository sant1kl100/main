from pygame import *
from random import randint

init()

class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, player_width=65, player_height=65):
    super().__init__()
    self.image = transform.scale(image.load(player_image), (player_width, player_height))    
    self.speed = player_speed
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y 
  def reset(self):
    win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  def update(self):
    keys = key.get_pressed()
    if (keys[K_LEFT] or keys[K_a]) and self.rect.x > 5:
      self.rect.x -= self.speed
    if (keys[K_RIGHT] or keys[K_d]) and self.rect.x < win_width - 80:
      self.rect.x += self.speed

win_width = 700
win_height = 500
win =  display.set_mode((win_width, win_height))
display.set_caption("мега шутер бета альфа ультра тест ранній доступ")

player = Player("circle.png", 200,200,5,65,65)
while True:
  player.update()