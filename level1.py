import pygame
import random


def lvl_1(sfx):  # shot):
    # global but
    pygame.init()
    win = pygame.display.set_mode((920, 550))
    pygame.display.set_caption('SLYм3')
    pygame.time.Clock()
    bg = pygame.image.load('background1.jpg')

    # sound effects

    jump = pygame.mixer.Sound('jump.wav')
    shoot = pygame.mixer.Sound('bullet.wav')
    death = pygame.mixer.Sound('death.wav')

    pygame.mixer.Sound.set_volume(jump, sfx)
    pygame.mixer.Sound.set_volume(shoot, sfx)
    pygame.mixer.Sound.set_volume(death, sfx)

    pygame.init()
    win = pygame.display.set_mode((920, 550))
    pygame.display.set_caption('Game')
    clock = pygame.time.Clock()
    bg = pygame.image.load('background1.jpg')

    score = 0

    def scorekeeper(score):
        s = pygame.time.get_ticks()
        score = score + float(s / 1000)

        return int(score)

    # this class defines all the properties and functions of our player
    class player:

        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 7
            self.isJump = False
            self.jumpCount = 10
            self.left = False
            self.right = False
            self.standing = True
            self.walkCount = 0
            self.health = 60

        def jump(self):
            if not self.isJump:
                if keys[pygame.K_UP]:
                    self.isJump = True
                    pygame.mixer.Sound.play(jump)
            else:
                if self.jumpCount >= -10:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= (self.jumpCount ** 2) * 0.5 * neg
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 10

        def draw(self, x, y, width, height):
            pygame.draw.rect(win, (0, 225, 0), (x, y, width, height))
            pygame.draw.rect(win, (200, 0, 0), (x - 20, y - 20, 60, 10))
            pygame.draw.rect(win, (0, 225, 0), (x - 20, y - 20, 60 - (60 - self.health), 10))

    class bullet:
        def __init__(self, x, y, radius, color, facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing

        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    class enemy:
        walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                    pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                    pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                    pygame.image.load('L1E.png')]
        walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                     pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                     pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                     pygame.image.load('R1E.png')]

        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isJump = False
            self.jumpCount = 7
            self.dodge = False
            self.walkCount = 0

        def move(self):
            if player1.x > self.x + 30:
                self.x += self.vel
            elif player1.x + 30 < self.x:
                self.x -= self.vel

        def jump(self):

            if not self.isJump:
                # if keys[pygame.K_SPACE]:
                self.isJump = True
            else:
                if self.jumpCount >= -7:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= (self.jumpCount ** 2) * 0.5 * neg
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 7
                    self.dodge = False

        def draw(self, win):
            # pygame.draw.rect(win,(225,0,0),(self.x,self.y,self.width,self.height))
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            # if enemy is left of player it will face right (towards the player)
            if self.x < player1.x:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

    player1 = player(00, 500, 20, 50)

    # enemy1=enemy(720,500,20,60)
    def redrawGameWindow():
        win.blit(bg, (0, 0))
        if player1.health > 0:
            player1.draw(player1.x, player1.y, player1.width, player1.height)

        for i in enemies:
            i.draw(win)
        # enemy1.draw(enemy1.x,enemy1.y,enemy1.width,enemy1.height)
        for i in bullets:
            i.draw(win)
        pygame.display.update()

    run = True
    # the main loop (keeps the game running till its closed)
    bullets = []
    enemies = []
    cooldown = 0
    wave = 0

    while run:
        clock.tick(27)
        if cooldown > 0:
            cooldown += 1
        if cooldown > 4:
            cooldown = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if len(enemies) == 0:
            for i in range(3 + wave):
                enemies.append(enemy(random.randint(0, 720), 500, 20, 60))
            wave = wave + 3
        for i in enemies:
            if abs(i.x - player1.x) < 35 and player1.y == 500:
                player1.health -= 0.5
                if player1.health == 0:
                    pygame.mixer.Sound.play(death)
                    print(scorekeeper(score))

        # code checks for collisions and also makes enemies dodge attacks

        for i in bullets:
            for j in enemies:
                if i.facing == -1:
                    if (120 < abs(i.x - j.x) < 180) and i.x > j.x and i.y > 520:
                        # enemies.pop(enemies.index(j))
                        if random.randint(0, 3) == 1:
                            j.dodge = True
                            continue
                    if abs(i.x - j.x) < 50 and j.dodge == False and i.x > j.x and i.y > 520:
                        enemies.pop(enemies.index(j))
                        bullets.pop(bullets.index(i))
                        break

                else:
                    if (100 < abs(i.x - j.x) < 130) and i.x < j.x and i.y > 520:
                        # enemies.pop(enemies.index(j))
                        if random.randint(0, 1) == 1:
                            j.dodge = True
                            continue
                    if abs(i.x - j.x) < 50 and j.dodge == False and i.x < j.x and i.y > 520:
                        enemies.pop(enemies.index(j))
                        bullets.pop(bullets.index(i))
                        break
                        # bullets.pop(bullets.index(i))

        for i in bullets:
            if 920 > i.x > 0:
                i.x += i.vel
            else:
                bullets.pop(bullets.index(i))
        keys = pygame.key.get_pressed()

        # if shot == 0:
        #     but = pygame.K_q
        # elif shot == 1:
        #     but = pygame.K_SPACE

        if keys[pygame.K_SPACE] and cooldown == 0:
            pygame.mixer.Sound.play(shoot)
            if player1.left:
                facing = -1
                # tomoveleft
            else:
                facing = 1
                # shootright
            # restricts n.o of bullets
            if len(bullets) < 5:
                bullets.append(
                    bullet(round(player1.x + player1.width // 2), round(player1.y + player1.height // 2), 6, (0, 0, 0),
                           facing))
            cooldown = 1
        if keys[pygame.K_LEFT] and player1.x > player1.vel:

            player1.left = True
            player1.right = False
            player1.x -= player1.vel
        elif keys[pygame.K_RIGHT] and player1.x < 920 - player1.width - player1.vel:

            player1.left = False
            player1.right = True
            player1.x += player1.vel

        player1.jump()
        # enemy1.move()
        for i in enemies:
            for j in enemies:
                if i.x + i.vel == j.x:
                    break
            else:
                i.move()
        for i in enemies:
            # i.move()
            if i.dodge:
                i.jump()

        redrawGameWindow()
