import pygame
import pygame_widgets
from pygame_widgets.slider import Slider

pygame.init()

# game window size
h = 920
w = 550
window = pygame.display.set_mode((h, w))
mainClock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('theme.ogg')
pygame.mixer.music.play(loops=-1)

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
bg = pygame.image.load("main_menu.png")

# settings

mv = smallfont.render('Music ', True, lime)
mvs = Slider(window,500, 230, 100, 15, min=0, max=100, step=1, initial=100, handleColour=(0, 0, 102), handleRadius=5, colour=(0, 153, 51))

# high scores text

# game menu text
l_1 = font.render(' Level 1', True, white)


# functions

def main_menu():
    click = False

    while True:
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
        mainClock.tick(60)


def game():
    running = True
    click = False

    while running:
        window.blit(bg, (0, 0))
        mx, my = pygame.mouse.get_pos()

        lvl_1 = pygame.Rect(375, 295, 150, 45)
        back = pygame.Rect(845, 0, 75, 75)

        if lvl_1.collidepoint((mx, my)):
            if click:
                pass  # lvl_1()
        if back.collidepoint((mx, my)):
            if click:
                main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        window.blit(l_1, (375, 295))
        window.blit(b, (845, 0))

        pygame.display.update()
        mainClock.tick(60)


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
        mainClock.tick(60)


main_menu()
