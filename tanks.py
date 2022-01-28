import this
from bullets import bullet

class tank:
    speed = 5
    rotationSpeed = 2
    rotation = 0
    pos_x = 0
    pos_y = 0
    def __init__(speed):
        this.speed = speed
    def turnLeft(target):
        this.rotation -= this.rotationSpeed
        if this.rotation <= 0:
            this.rotation = 0
        if this.rotation <= target:
            this.rotation = target
    def turnRight(target):
        this.rotation += this.rotationSpeed
        if this.rotation >= 360:
            this.rotation = 0
        if this.rotation >= target:
            this.rotation = target
    def moveForward():
        if this.rotation == 0:
            this.pos_y -= this.speed
        if this.rotation == 90:
            this.pos_x += this.speed
        if this.rotation == 180:
            this.pos_y += this.speed
        if this.rotation == 270:
            this.pos_x -= this.speed
    def fireBullet():
        pass

class enemyTank(tank):
    def pathfinding():
        pass