from pygame import*


window = display.set_mode((750,653))
display.set_caption(('Why are you reading this?'))
# #задай фон сцены
background=transform.scale(image.load('nice.png'),(750,653))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.width = w
        self.high = h
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 653-self.high:
            self.rect.y += self.speed




class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < 653-self.high:
            self.rect.y += self.speed


player1 = Player1('uno.jpg', 53, 325, 24, 100, 150)

player2 = Player2('dos.jpg', 600, 325, 24, 100, 150)



mixer.init()
mixer.music.load('pvz.mp3')
# AudioSegment.from_mp3("dio.mp3").export('dio.ogg', format='ogg')
mixer.music.play()








game = True
while game:
    window.blit(background,(0,0))
    player1.update()
    player1.reset()
    player2.update()
    player2.reset()
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()