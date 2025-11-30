import pygame
import random

class Food:
    def __init__(self, width=20, height=20, screen_width=600, screen_height=400):
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (self.screen_width - self.width)//self.width) * self.width
        y = random.randint(0, (self.screen_height - self.height)//self.height) * self.height
        return (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), (*self.position, self.width, self.height))
