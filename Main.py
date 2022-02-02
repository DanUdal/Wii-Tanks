import this
import pyglet
from tanks import tank
from bullets import bullet
from levels import gameObjects
from levels import tanks
from pyglet.libs.win32.constants import TRUE
from pyglet.window import key

def turn(tank, target): #turn tank to target direction or move in that direction if already facing it
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

def on_key_press(symbol, modifiers): #movement controls
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

def on_key_release(symbol, modifiers): #if a button is released then finish current turn and stop
    if symbol == key.W:
        stop = True
    if symbol == key.D:
        stop = True
    if symbol == key.S:
        stop = True
    if symbol == key.A:
        stop = True

def update(): #call the update function for all game objects for any process that occurs every frame
    global gameObjects
    for i in gameObjects:
        i.update()
    if len(tanks) == 0:
        #end level if all enemies are destroyed
        pass

playerTank = tank() #the player's tank
gameObjects.append(playerTank)

turning = False

stop = False

window = pyglet.window.Window() #open a window to display the game

pyglet.clock.schedule_interval(update, 1/120)

pyglet.app.run()