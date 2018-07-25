'''Lowest Number of Shots needed 
to hit the battleship in Battleship
from Algorithmic Puzzles, Levitin 
July 24, 2018'''

import random

NUM_R = 10
NUM_C = 10

class Cell:
    def __init__(self,x,y,sz,occupied=False):
        self.x = x
        self.y = y
        self.sz = sz
        self.occupied = occupied
        
    def update(self):
        if self.occupied:
            fill(100)
        else:
            fill(255)
        rect(self.x,self.y,self.sz,self.sz)
        
class Grid:
    def __init__(self):
        self.m = NUM_R
        self.n = NUM_C
        self.cellList = [Cell(sz*x,sz*y,sz) \
                         for y in range(self.m) \
                         for x in range(self.n)]
        
    def update(self):
        for c in self.cellList:
            c.update()
            
            
class Battleship:
    def __init__(self):
        self.x = random.randint(0,NUM_C-1)
        self.y = random.randint(0,NUM_R-1)
        while NUM_C - self.x < 4:
            self.x = random.randint(0,NUM_C-1)
        while NUM_R - self.y < 4:
            self.y = random.randint(0,NUM_R-1)
            
        #choose direction 0 = horiz, 1 = vert
        self.direction = random.randint(0,1) 
        if self.direction == 0: #horizontal
            self.squares = [[self.x+i,self.y] for i in range(4)]
              
        else: #vertical
            self.squares = [[self.x,self.y+i] for i in range(4)]
        
    '''def update(self):
        fill(100)
        for i in self.squares:
            rect(i[0]*sz,i[1]*sz,sz,sz)'''
        
            
class Shot:
    '''returns True if scores a Hit!'''
    def __init__(self,c,r):
        self.r = r
        self.c = c
        
    def shoot(self,grid):
        fill(255,0,0)
        ellipse(self.c*sz,self.r*sz,sz,sz)
        if grid.cellList[NUM_C*self.r + self.c].occupied:
                return True
        
class Game:
    def __init__(self):
        self.grid = Grid()
        self.ship = Battleship()
        for s in self.ship.squares:
            self.grid.cellList[self.grid.n*s[1]+s[0]].occupied = True
        println("ship")
        println(self.ship.squares)
                
    def play(self):
        global hits
        #self.ship.update()
        self.grid.update()
        self.shot = Shot(random.randint(0,NUM_C-1),
                         random.randint(0,NUM_R-1))
        self.shot = Shot(4,2)
        println("shot")
        println([self.shot.r,self.shot.c])
        hit = self.shot.shoot(g)
        textSize(18)
        if hit:
            hits += 1
            fill(0,255,0) #green
            text("HIT!",50,50)
        else:
            fill(255,0,0) #red
            text("MISS!",50,50)

def setup():
    global sz,g,hits
    size(600,600)
    ellipseMode(CORNER)
    sz = width/10.0
    g = Grid()
    hits = 0
    
def draw():
    frameRate(4)
    background(255)
    #global g
    g.update()
    game1 = Game()
    game1.play()
    fill(0,0,255)
    text("HITS: "+str(hits),500,10)
