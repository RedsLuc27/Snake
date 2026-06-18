import pygame
from pygame.locals import *
import random

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Snake():
    
    def __init__(self):
        self.snake = [(200,200),(210,200),(220,200),(230,200),(240,200)]
        self.skin = pygame.Surface((10,10))
        self.skin.fill((000,000,255))
        self.head = pygame.Surface((10,10))
        self.head.fill((10,10,200))
        self.direction = RIGHT

    def crawl(self):
        score = self.Score()

        x, y = self.snake[-1]

        directions = {
            RIGHT: (10, 0),
            LEFT: (-10, 0),
            UP: (0, -10),
            DOWN: (0, 10)
        }

        dx, dy = directions[self.direction]

        new_head = (x + dx, y + dy)
        
        if score < 10:
            prob = False
        elif score < 20:
            prob = random.randint(1, 10) > 2
        elif score < 30:
            prob = random.randint(1, 10) > 4
        elif score < 50:
            prob = random.randint(1, 10) > 6
        else:
            prob = random.randint(1, 10) > 8

        self.snake.append(new_head)

        if not prob:
            self.snake.pop(0)


    def snake_eat_apple(self, apple_pos):
        return self.snake[-1] == apple_pos
    
    def snake_bigger(self):
        self.snake.insert(0, (self.snake[0]))

    def self_collision(self):
        return self.snake[-1] in self.snake[0:-1]

    def wall_collision(self, screen_size):
        return self.snake[len(self.snake)-1][0]>=screen_size or self.snake[len(self.snake)-1][0]<0 or self.snake[len(self.snake)-1][1]>=screen_size or self.snake[len(self.snake)-1][1]<0
    
    def Score(self) -> int:
        return len(self.snake)-5
    
    def get_snake(self):
        return self.snake

class Apple():

    snake = Snake()
    def __init__(self):
        self.apple = pygame.Surface((10,10))
        self.apple.fill((255,0,0))
        self.position = (0,0)

    def set_random_position(self, screen_size):
        self.position = (random.randrange(0, screen_size-10, 10), random.randrange(0, screen_size-10, 10))
        if self.position in self.snake.get_snake():
            self.set_random_position(screen_size)