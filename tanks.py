from turtle import position
from bullets import bullet
from levels import gameObjects

class tank:
    speed = 5
    rotationSpeed = 2
    rotation = 0
    position = []
    gunDirection = []
    def __init__(self, speed):
        self.speed = speed
    def turnLeft(self, target):
        self.rotation -= self.rotationSpeed
        if self.rotation <= 0:
            self.rotation = 0
        if self.rotation <= target:
            self.rotation = target
    def turnRight(self, target): #rotate the target direction and defined speed
        self.rotation += self.rotationSpeed
        if self.rotation >= 360:
            self.rotation = 0
        if self.rotation >= target:
            self.rotation = target
    def moveForward(self): #move forward at defined speed
        if self.rotation == 0:
            self.pos_y -= self.speed
        if self.rotation == 90:
            self.pos_x += self.speed
        if self.rotation == 180:
            self.pos_y += self.speed
        if self.rotation == 270:
            self.pos_x -= self.speed
    def fireBullet(self): #instantiate and bullet in the gameobjects list
        gameObjects.append(bullet(self.position, self.gunDirection))
    def update(self):
        pass

class enemyTank(tank):
    def pathfinding(): #run the A* algorithm to determine the tank's path through the level
        pass