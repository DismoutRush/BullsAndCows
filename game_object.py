from pygame.rect import Rect
import pygame
import colors

class GameObject:
    def __init__(self, x, y, w, h, color=colors.PUMICE):
        self.bounds = Rect(x, y, w, h)
        self.color = color

    @property
    def left(self):
        return self.bounds.left

    @property
    def right(self):
        return self.bounds.right

    @property
    def top(self):
        return self.bounds.top

    @property
    def bottom(self):
        return self.bounds.bottom

    @property
    def width(self):
        return self.bounds.width

    @property
    def height(self):
        return self.bounds.height

    @property
    def center(self):
        return self.bounds.center

    @property
    def centerx(self):
        return self.bounds.centerx

    @property
    def centery(self):
        return self.bounds.centery

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds, border_radius=30)

    def update(self):
        pass

