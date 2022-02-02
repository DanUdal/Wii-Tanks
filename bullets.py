from random import randbytes
from turtle import speed
from levels import gameObjects

class ray:
    direction = [1,0]
    endPoint = [1,0]
    def __init__(self, direction):
        self.direction = direction
    @staticmethod
    def findCollision(bullet, direction):
        rays = []
        for i in range(0, bullet.bounces + 1):
            rays[i] = ray(direction)
            #check for a collision with any walls in the level
            #set end point to point of collision
        return rays

class bullet:
    speed = 10
    rays = []
    bounces = 1
    position = []
    def __init__(self, position, direction):
        self.rays = ray.findCollision(self, direction)
    def update(self):
        if abs(self.position - self.rays.endPoint) < 2: 
            #if within 2 pixels of the collision point to ensure it never misses the bounce from rounding errors
            self.position += self.rays[0] * self.speed
        else:
            self.rays.pop(0) #if at end point remove current ray and move to next
            if len(self.rays) != 0:
                self.position += self.rays[0] * self.speed
            else: #if no rays left destroy bullet
                self.destroy()
    def destroy(self):
        gameObjects.remove(self)
        del self
    def collision(self): #check for a collision with a tank or bullet
        #loop from game objects to see if bullet is intersecting any
        #destroy both objects if there is a collision
        pass