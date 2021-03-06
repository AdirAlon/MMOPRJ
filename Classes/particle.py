import math
import time

import pygame


class Particle:
    id = 0

    def __init__(self, x, y, target_x, target_y, speed, range, dmg, name):
        self.id_of_particle = Particle.id
        Particle.id += 1
        Particle.id %= 1000
        self.x = x
        self.y = y
        self.angle = math.atan2(float(self.y - target_y), float(self.x - target_x))
        self.speed = speed
        self.range = range
        self.first_move = True
        self.hit = False
        self.dmg = dmg
        self.last_moved = 0
        self.velocity_x = float(self.speed * math.cos(self.angle))
        self.velocity_y = float(self.speed * math.sin(self.angle))
        self.angle *= -180 / math.pi
        self.image = pygame.image.load(f'../Assets/weapons/{name}.png')
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.hit_box = self.image.get_rect()
        self.hit_box.center = self.x, self.y
        self.name = name

    def move(self, entity) -> bool:
        if time.time() - self.last_moved > 10 ** -3:
            self.first_move = False
            if self.speed == 1:
                self.x, self.y = entity.x, entity.y
                self.x -= self.velocity_x * (120 - self.range)
                self.y -= self.velocity_y * (120 - self.range)
            self.last_moved = time.time()
            self.x -= self.velocity_x
            self.y -= self.velocity_y
            self.hit_box.center = int(self.x), int(self.y)
            self.range -= self.speed
            return True
        return False
