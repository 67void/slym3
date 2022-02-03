import pygame


def lvl_1():
    pygame.init()
    win = pygame.display.set_mode((920, 550))
    pygame.display.set_caption('Game')
    clock = pygame.time.Clock()
    bg = pygame.image.load('background1.jpg')
    slime = pygame.mixer.Sound('slime.wav')

    # this class defines all the properties and functions of our player
    class player:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isJump = False
            self.jumpCount = 10
            self.left = False
            self.right = False
            self.standing = True
            self.walkCount = 0

        def draw(self, x, y, width, height):
            pygame.draw.rect(win, (225, 0, 0), (x, y, width, height))

    player1 = player(700, 500, 20, 50)

    def redrawGameWindow():
        win.blit(bg, (0, 0))
        player1.draw(player1.x, player1.y, player1.width, player1.height)
        pygame.display.update()

    run = True
    # the main loop (keeps the game running till its closed)
    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player1.x > player1.vel:
            player1.x -= player1.vel
        elif keys[pygame.K_RIGHT] and player1.x < 920 - player1.width - player1.vel:
            player1.x += player1.vel
        if not player1.isJump:
            if keys[pygame.K_SPACE]:
                player1.isJump = True
                slime.play()
        else:
            if player1.jumpCount >= -10:
                neg = 1
                if player1.jumpCount < 0:
                    neg = -1
                player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
                player1.jumpCount -= 1
            else:
                player1.isJump = False
                player1.jumpCount = 10

        redrawGameWindow()
