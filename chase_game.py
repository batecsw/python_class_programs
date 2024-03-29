import random

WIDTH = 600
HEIGHT = 600

background = Actor("sand")
player = Actor("idle__000")
player.x = 200
player.y = 200

enemy = Actor("fly")
player2 = Actor("idle1")
coin = Actor("coingold", pos=(300,300))
score = 0
time = 20


def draw():
    screen.clear()
    background.draw()
    player.draw()
    enemy.draw()
    player2.draw()
    coin.draw()
    screen.draw.text("My game", (200,0), color='red')
    score_string = str(score)
    screen.draw.text(score_string, (0,0), color='green')
    time_string = str(round(time))
    screen.draw.text(time_string, (50,0), color='green')

def update(delta):
    global score, time
    time = time - delta
    if time <= 0:
        exit()
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0

    if enemy.x < player.x:
        enemy.x = enemy.x + 1
    if enemy.x > player.x:
        enemy.x = enemy.x - 1
    if enemy.y < player.y:
        enemy.y = enemy.y + 1
    if enemy.y > player.y:
        enemy.y = enemy.y - 1
    if player.colliderect(enemy):
        exit()

    if keyboard.d:
        player2.x = player2.x + 4
    if keyboard.a:
        player2.x = player2.x - 4
    if keyboard.s:
        player2.y = player2.y + 4
    if keyboard.w:
        player2.y = player2.y - 4
    if player.colliderect(player2):
        exit()

    if coin.colliderect(player):
        coin.x = random.randint(0, WIDTH)
        coin.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score:", score)
