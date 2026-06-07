import pygame
from pygame.locals import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Snake():
    
    def __init__(self):
        self.snake = [(200,200),(210,200),(220,200),(230,200),(240,200)]
        self.skin = pygame.Surface((10,10))
        self.skin.fill((255,255,255))
        self.head = pygame.Surface((10,10))
        self.head.fill((200,200,200))
        self.direction = RIGHT

    def crawl(self):
        if self.direction == RIGHT:
            self.snake.append((self.snake[len(self.snake)-1][0] + 10, self.snake[len(self.snake)-1][1]))
        elif self.direction==UP:
            self.snake.append((self.snake[len(self.snake)-1][0] , self.snake[len(self.snake)-1][1] -10))
        elif self.direction==DOWN:
            self.snake.append((self.snake[len(self.snake)-1][0] , self.snake[len(self.snake)-1][1] + 10))
        elif self.direction==LEFT:
            self.snake.append((self.snake[len(self.snake)-1][0] -10 , self.snake[len(self.snake)-1][1]))
        self.snake.pop(0)