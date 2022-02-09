"""
1.创建坦克，子弹，砖块，不锈钢，湖泊对象
２．不同对象分配不同的属性与方法；
３．主函数
"""
import random
import sys
import time
import os
import pygame
from urllib.request import urlretrieve

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
BRICK_WIDTH = 20
BRICK_HEIGHT = 30


def load_image(name_img):
    save = Tank_IMAGE_POSITION + os.sep + name_img + '.gif'
    if not os.path.exists(save):
        urlretrieve(URL + name_img + '.gif', save)
    return pygame.image.load(save)

def load_music(name_music):
    save = Tank_IMAGE_POSITION + os.sep + name_music + '.wav'
    if not os.path.exists(save):
        urlretrieve(URL + name_music + '.wav', save)
    pygame.mixer.music.load(save)
    pygame.mixer.music.play()

class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Tank():
    def __init__(self, left, top, window, image, direction, speed):
        super().__init__()
        self.window = window
        self.direction = direction
        self.speed = speed
        self.load_image = image
        self.img = self.load_image[self.direction]
        self.rect = self.img.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.tank_width = self.rect.width
        self.tank_height = self.rect.height
        self.wall_switch = False
        self.move_stop = True
        self.live = True
        self.old_left = 0
        self.old_top = 0

    def fire(self):
        return Bullet(self, self.window)

    def display(self):
        self.img = self.load_image[self.direction]
        self.window.blit(self.img, self.rect)

    def wall_not(self, direction):
        if direction == 'U':
            return self.rect.top > 0
        elif direction == 'D':
            return self.rect.top <= SCREEN_HEIGHT - self.tank_height
        


class bullet(BaseItem):
    def __init__(self, speed):
        self.speed = speed;


class brick():
    def __init__(self, width, height ):
        self.width = width;
        self.height = height;

class Main():
    def startGame():


