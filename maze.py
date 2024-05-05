#создай игру "Лабиринт"!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
       window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 395:
            self.rect.x += self.speed

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 395:
           self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
              self.direction = 'right'
        if self.rect.x >= 620:
              self.direction = 'left'


        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load("background.jpg"), (700, 500))
player = Player('hero.png',5,70,4)
monster = Enemy('cyborg.png',600,280,4)
treasure = GameSprite('treasure.png',650,310,4)
walll = Wall(154,205,50,100,20,450,10)
walll2 = Wall(154,205,50,100,480,450,10)
walll3 = Wall(154,205,50,100,20,10,380)
walll4 = Wall(154,205,50,200,100,10,380)
walll5 = Wall(154,205,50,300,20,10,380)
walll6 = Wall(154,205,50,400,100,10,380)
game = True
speed = 1
clock = time.Clock()
FPS = 60
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()
        treasure.reset()
        walll.draw_wall()
        walll2.draw_wall()
        walll3.draw_wall()
        walll4.draw_wall()
        walll5.draw_wall()
        walll6.draw_wall()


        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, walll) or sprite.collide_rect(player, treasure):
            finish = True
            money.play()
    display.update()
    clock.tick(FPS)