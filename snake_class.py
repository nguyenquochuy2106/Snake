import pygame

class Snake:
    def __init__(self):
        self.size = 20
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"
        self.grow_flag = False

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= self.size
        elif self.direction == "DOWN":
            y += self.size
        elif self.direction == "LEFT":
            x -= self.size
        elif self.direction == "RIGHT":
            x += self.size
        self.body.insert(0, (x, y))
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def grow(self):
        self.grow_flag = True

    def change_direction(self, new_direction):
        # Không cho rẽ ngược
        opposite = {"UP":"DOWN","DOWN":"UP","LEFT":"RIGHT","RIGHT":"LEFT"}
        if new_direction != opposite[self.direction]:
            self.direction = new_direction

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (0,255,0), (*segment, self.size, self.size))
