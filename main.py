from pygame import *

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
window = display.set_mode((700, 500))
display.set_caption("Shooter")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
sprite1 = transform.scale(image.load("rocket.png"), (100, 100))
#sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))

x1, y1 = 300, 390
x2, y2 = 400, 300
speed = 10
clock = time.Clock()
FPS = 60
game = True
while game:
    window.blit(background, (0,0))
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if keys[K_s] and y1 < 390:
        y1 += speed
    if keys[K_w] and y1 > 5:
        y1 -= speed
    if keys[K_a] and x1 >5:
        x1 -= speed
    if keys[K_d] and x1 < 600:
        x1 += speed

    window.blit(sprite1, (x1,y1))
    #window.blit(sprite2, (x2,y2))
    display.update()
    clock.tick(FPS)