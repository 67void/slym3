import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
import level1
# import test
import sys
import time

pygame.init()  # game initialised

# related to window
w, h = 920, 550
window = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.display.set_caption('SLYм3')
icon = pygame.image.load('icon.jpeg')
pygame.display.set_icon(icon)
pygame.mixer.init()
pygame.mixer.music.load('Arcane OST ENEMY (League of Legends) Orchestral Remix.ogg')
pygame.mixer.music.play(loops=-1)
bg = pygame.image.load("main_menu.png")
bgs = pygame.image.load("settings.jpg")
bgh = pygame.image.load("highscores_temp.jpg")

# colors list

white = (255, 255, 255)
aqua = (0, 255, 255)
black = (0, 0, 0)
green = (102, 255, 102)
lime = (204, 255, 153)
red = (255, 0, 0)
blue = (51, 102, 255)

# fonts list

font = pygame.font.SysFont('century gothic', 35)
smallfont = pygame.font.SysFont('century gothic', 20)
largefont = pygame.font.SysFont('century gothic', 60)
ultrafont = pygame.font.SysFont('century gothic', 160)


# main menu text

def d_txt(text, ft, color, surface, x, y):
    txt = ft.render(text, True, color)
    txt_pos = (x, y)
    surface.blit(txt, txt_pos)


def slide(stype, x, y):
    mx, my = pygame.mouse.get_pos()
    if stype == "slide_1":
        if x <= mx <= x + 150 and y <= my <= y + 45:
            slide_1 = pygame.surface.Surface((150, 45))
            pygame.surface.Surface.set_alpha(slide_1, 75)
            window.blit(slide_1, (x, y))
    if stype == "slide_2":
        if x <= mx <= x + 75 and y <= my <= y + 75:
            slide_2 = pygame.surface.Surface((65, 65))
            pygame.surface.Surface.set_alpha(slide_2, 75)
            window.blit(slide_2, (x, y))
    if stype == "slide_3":
        if x <= mx <= x + 150 and y <= my <= y + 40:
            slide_1 = pygame.surface.Surface((150, 40))
            pygame.surface.Surface.set_alpha(slide_1, 75)
            window.blit(slide_1, (x, y))


# settings
mvs = Slider(window, 500, 230, 100, 15, min=0, max=100, step=1, initial=100, handleColour=blue, handleRadius=5,
             colour=lime)
sfxs = Slider(window, 500, 250, 100, 15, min=0, max=100, step=1, initial=100, handleColour=blue, handleRadius=5,
              colour=lime)

# game menu
jump = pygame.mixer.Sound('jump.wav')


# functions
def start():
    rt = ultrafont.render("SLYм3", True, red)
    t = smallfont.render(" Hit ↑ to skip ", True, (150, 0, 0))
    text_rect = rt.get_rect(center=(w / 2, h / 2))
    tr = t.get_rect(center=(w / 2, h / 2 + 150))
    # Show some texts fade in/out

    FADE_IN_TIME = 5
    FADE_OUT_TIME = 5
    FADE_IN_EASING = lambda x: x  # Linear
    FADE_OUT_EASING = lambda x: x  # Linear

    ST_FADEIN = 0
    ST_FADEOUT = 1

    state = ST_FADEIN
    last_state_change = time.time()

    while 1:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Exit the main loop
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_menu()

        # Update the state
        state_time = time.time() - last_state_change

        if state == ST_FADEIN:
            if state_time >= FADE_IN_TIME:
                state = ST_FADEOUT
                # state_time = max(0, min(state_time - FADE_IN_TIME, 1))
                state_time -= FADE_IN_TIME
                last_state_change = time.time() - state_time

        elif state == ST_FADEOUT:
            if state_time >= FADE_OUT_TIME:
                state = ST_FADEIN
                # state_time = max(0, min(state_time - FADE_OUT_TIME, 1))
                state_time -= FADE_OUT_TIME
                last_state_change = time.time() - state_time

        else:
            raise ValueError()

        if state == ST_FADEIN:
            alpha = FADE_IN_EASING(1.0 * state_time / FADE_IN_TIME)

        else:
            main_menu()

        surf2 = pygame.surface.Surface((text_rect.width, text_rect.height))
        surf3 = pygame.surface.Surface((tr.width, tr.height))
        surf2.set_alpha(255 * alpha)

        window.fill((0, 0, 0))
        surf2.blit(rt, (0, 0))
        surf3.blit(t, (0, 0))
        window.blit(surf2, text_rect)
        window.blit(surf3, tr)

        pygame.display.flip()
        clock.tick(60)


def main_menu():
    running = True
    click = False

    while running:
        window.blit(bg, (0, 0))
        mx, my = pygame.mouse.get_pos()

        d_txt('    play', font, green, window, 375, 295)
        d_txt('       settings', smallfont, lime, window, 375, 430)
        d_txt(' x', largefont, white, window, 845, 0)

        g_button = pygame.Rect(375, 295, 150, 45)
        s_button = pygame.Rect(375, 430, 150, 40)
        q_button = pygame.Rect(845, 0, 75, 75)

        slide("slide_1", 375, 295)
        slide("slide_3", 375, 430)
        slide("slide_2", 845, 10)

        if g_button.collidepoint((mx, my)):
            if click:
                game()
        if s_button.collidepoint((mx, my)):
            if click:
                settings()
        if q_button.collidepoint((mx, my)):
            if click:
                quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


def game():
    running = True
    click = False

    while running:
        window.blit(bg, (0, 0))
        mx, my = pygame.mouse.get_pos()

        d_txt(' <', largefont, white, window, 845, 0)
        d_txt(' Level 1', font, white, window, 375, 295)
        d_txt(' Level 2', font, white, window, 375, 355)

        lvl_1 = pygame.Rect(375, 295, 150, 45)
        lvl_2 = pygame.Rect(375, 355, 150, 45)
        back = pygame.Rect(845, 0, 75, 75)

        slide("slide_1", 375, 295)
        slide("slide_1", 375, 355)
        slide("slide_2", 850, 5)

        if lvl_1.collidepoint((mx, my)):
            if click:
                sfx = sfxs.getValue() * 0.01
                level1.lvl_1(sfx)
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

        pygame.display.update()
        clock.tick(60)


def settings():
    running = True
    click = False

    while running:
        window.blit(bgs, (0, 0))
        mx, my = pygame.mouse.get_pos()

        d_txt(' <', largefont, white, window, 845, 0)
        d_txt('Music ', smallfont, lime, window, 310, 220)
        d_txt('Sound Effects', smallfont, lime, window, 240, 250)

        back = pygame.Rect(845, 0, 75, 75)
        slide("slide_2", 850, 5)

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
        pygame.mixer.Sound.set_volume(jump, sfxs.getValue() * 0.01)

        pygame_widgets.update(pygame.event.get())
        pygame.display.update()


start()
