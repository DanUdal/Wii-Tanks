import this
import pyglet
from pyglet.libs.win32.constants import TRUE
from pyglet.window import key

class ray:
    direction = [1,0]
    endPoint = [1,0]

class bullet:
    speed = 10
    rays = []


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
            this.pos_y += this.speed
        if this.rotation == 90:
            this.pos_x += this.speed
        if this.rotation == 180:
            this.pos_y -= this.speed
        if this.rotation == 270:
            this.pos_x -= this.speed

def turn(tank, target):
    turning = True
    if tank.rotation != target:
        if abs(target - tank.rotation) > 0:
            tank.turnRight(target)
        else:
            tank.turnLeft(target)
    else:
        if stop != True:
            tank.moveForward()
        else:
            pyglet.clock.unschedule(turn)
            global stop
            stop = False

def on_key_press(symbol, modifiers):
    if symbol == key.W:
        if turning == True:
            pyglet.clock.unschedule(turn)
        pyglet.clock.schedule_interval(turn(playerTank, 0), 1/120)
    if symbol == key.D:
        if turning == True:
            pyglet.clock.unschedule(turn)
        pyglet.clock.schedule_interval(turn(playerTank, 90), 1/120)
    if symbol == key.S:
        if turning == True:
            pyglet.clock.unschedule(turn)
        pyglet.clock.schedule_interval(turn(playerTank, 180), 1/120)
    if symbol == key.A:
        if turning == True:
            pyglet.clock.unschedule(turn)
        pyglet.clock.schedule_interval(turn(playerTank, 270), 1/120)

def on_key_release(symbol, modifiers):
    if symbol == key.W:
        stop = True
    if symbol == key.D:
        stop = True
    if symbol == key.S:
        stop = True
    if symbol == key.A:
        stop = True

playerTank = tank()

turning = False

stop = False

window = pyglet.window.Window()

pyglet.app.run()