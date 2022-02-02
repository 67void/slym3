import pygame
import pygame_widgets
from pygame_widgets.slider import Slider

pygame.init()

# game win size
h, w = 920, 550
window = pygame.display.set_mode((h, w))
clock = pygame.time.Clock()
pygame.display.set_caption('SLYм3')
icon = pygame.image.load('icon.jpeg')
pygame.display.set_icon(icon)
pygame.mixer.init()
pygame.mixer.music.load('theme.ogg')
pygame.mixer.music.play(loops=-1)
bg = pygame.image.load("main_menu.png")
# colors

white = (255, 255, 255)
aqua = (0, 255, 255)
black = (0, 0, 0)
green = (102, 255, 102)
lime = (204, 255, 153)

# fonts

font = pygame.font.SysFont('century gothic', 35)
smallfont = pygame.font.SysFont('century gothic', 20)
largefont = pygame.font.SysFont('century gothic', 60)

# main menu text

g = font.render('    play', True, green)
s = smallfont.render('   settings', True, lime)
h = smallfont.render('   highscores', True, lime)
q = largefont.render('x', True, white)
b = largefont.render('<', True, white)


# settings

mv = smallfont.render('Music ', True, lime)
mvs = Slider(window, 500, 230, 100, 15, min=0, max=100, step=1, initial=100, handleColour=(0, 0, 102), handleRadius=5,
             colour=(0, 153, 51))

# high scores text

# game menu text
l_1 = font.render(' Level 1', True, white)
l_2 = font.render(' Level 2', True, white)


# functions

def main_menu():
    running = True
    click = False

    while running:
        window.blit(bg, (0, 0))
        mx, my = pygame.mouse.get_pos()

        g_button = pygame.Rect(375, 295, 150, 45)
        s_button = pygame.Rect(230, 430, 150, 40)
        h_button = pygame.Rect(506, 430, 150, 40)
        q_button = pygame.Rect(845, 0, 75, 75)

        if g_button.collidepoint((mx, my)):
            if click:
                game()
        if s_button.collidepoint((mx, my)):
            if click:
                settings()
        if h_button.collidepoint((mx, my)):
            if click:
                highscores()
        if q_button.collidepoint((mx, my)):
            if click:
                quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        window.blit(g, (375, 295))
        window.blit(s, (230, 430))
        window.blit(h, (506, 430))
        window.blit(q, (845, 0))

        pygame.display.update()
        clock.tick(60)


def game():
    running = True
    click = False

    while running:
        window.blit(bg, (0, 0))
        mx, my = pygame.mouse.get_pos()

        lvl_1 = pygame.Rect(375, 295, 150, 45)
        lvl_2 = pygame.Rect(375, 355, 150, 45)
        back = pygame.Rect(845, 0, 75, 75)

        if lvl_1.collidepoint((mx, my)):
            if click:
                def lvl1():

                    # this class defines all the properties and functions of our player
                    class player():
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
                            pygame.draw.rect(window, (225, 0, 0), (x, y, width, height))

                    player1 = player(700, 500, 20, 50)

                    def redrawGameWindow():
                        window.blit(bg, (0, 0))
                        player1.draw(player1.x, player1.y, player1.width, player1.height)
                        pygame.display.update()

                    def game():
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
                    game()
                lvl1()

        if back.collidepoint((mx, my)):
            if click:
                main_menu()

        if lvl_2.collidepoint((mx, my)):
            if click:
                pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        window.blit(l_1, (375, 295))
        window.blit(l_2, (375, 355))
        window.blit(b, (845, 0))

        pygame.display.update()
        clock.tick(60)


def settings():
    running = True
    click = False

    while running:
        mx, my = pygame.mouse.get_pos()
        back = pygame.Rect(845, 0, 75, 75)

        if back.collidepoint((mx, my)):
            if click:
                main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.mixer.music.set_volume(mvs.getValue() * 0.01)


        window.blit(b, (845, 0))
        window.blit(mv, (310, 220))
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()


def highscores():
    running = True
    click = False

    while running:
        mx, my = pygame.mouse.get_pos()
        back = pygame.Rect(845, 0, 75, 75)

        if back.collidepoint((mx, my)):
            if click:
                main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        window.blit(b, (845, 0))

        pygame.display.update()
        clock.tick(60)


main_menu()
