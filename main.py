
import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
surface = pygame.display.get_surface()
pygame.display.set_caption('GD', '\\pictures\\test.png')
icon = pygame.image.load(os.getcwd() + '\\pictures\\test.png')
pygame.display.set_icon(icon)
bg = pygame.image.load(os.getcwd() + '\\pictures\\menu.png')
pygame.display.flip()
width = surface.get_width()
height = surface.get_height()
buttons = {}


class Button(object):
    def __init__(self, image, rect, name):
        self.image = image
        self.rect = rect
        self.name = name
        buttons[name] = self
        self.button = pygame.Rect(rect[0], rect[1], rect[2], rect[3])

    def draw(self):
        screen.blit(self.image, [self.rect[0], self.rect[1]])

    def is_pressed(self, mouse_pos):
        if self.button.collidepoint(mouse_pos):
            return True
        else:
            return False


def main_menu(bg_menu, width_menu, height_menu):
    image_quit = (pygame.image.load(os.getcwd() + '\\pictures\\button_quit.png'))
    button = Button(image_quit, [width_menu - 100, 50, 50, 50], 'quit')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if buttons['quit'].is_pressed(mouse_pos):
                    pygame.quit()
                    return
        screen.fill(bg_menu)
        for button in buttons:
            buttons[button].draw()
        pygame.display.flip()


main_menu(bg, width, height)
