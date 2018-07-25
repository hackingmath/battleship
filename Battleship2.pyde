'''Lowest Number of Shots needed 
to hit the battleship in Battleship
from Algorithmic Puzzles, Levitin 
July 24, 2018'''

import time
import random

NUM_R = 10
NUM_C = 10

class Cell:
    '''A single square'''
    def __init__(self,y,x,sz,occupied=False):
        self.x = x
        self.y = y
        self.sz = sz
        self.occupied = occupied
        
    def update(self):
        if self.occupied:
            fill(100) #gray
        else:
            fill(255) #white
        rect(self.x,self.y,self.sz,self.sz)
        
class Grid:
    #m x n grid of cells
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
    #4x1 rectangle
    def __init__(self):
        self.x = random.randint(0,NUM_C-1)
        self.y = random.randint(0,NUM_R-1)
            
        #choose direction 0 = horiz, 1 = vert
        self.direction = random.randint(0,1) 
        if self.direction == 0: #horizontal
            self.y = random.randint(0,NUM_R-1) #row can be anything
            while NUM_C - self.x < 4: #column can't be less than 4 from the edge
                self.x = random.randint(0,NUM_C-1)
            self.squares = [[self.y,self.x+i] for i in range(4)]
              
        else: #vertical
            while NUM_R - self.y < 4:
                self.y = random.randint(0,NUM_R-1)
            self.x = random.randint(0,NUM_C-1)
            self.squares = [[self.y+i,self.x] for i in range(4)]
        
            
class Shot:
    '''returns True if scores a Hit!'''
    def __init__(self,r,c):
        self.r = r
        self.c = c
        
    def shoot(self,grid):
        
        index = NUM_C*self.r + self.c
        if grid.cellList[index].occupied:
                return True
        
class Game:
    def __init__(self):
        global grid
        grid = Grid() #create the Grid
        self.ship = Battleship() #create the Battleship
        #set the battleship's squares to be occupied
        for s in self.ship.squares:
            grid.cellList[grid.n*s[1]+s[0]].occupied = True
                
    def play(self):
        global hits,shots,shotsnum,games,shotList
        shotList = []
        shots = 0
        hit = False
        
        while not hit:
            #grid.update()
            #take a random shot
            self.shot = Shot(random.randint(0,NUM_C-1),
                            random.randint(0,NUM_R-1))\
            #put it in the shotList
            shotList.append([self.shot.c,self.shot.r])
            shots += 1 #increment the number of shots taken
            hit = self.shot.shoot(grid) #check for a hit
        grid.update() #draw the final grid of the game
        #draw the shots taken
        for shot in shotList:
            fill(255,0,0)
            ellipse(shot[1]*sz,shot[0]*sz,sz,sz)
        #time.sleep(0.5)
        games += 1
        shotsnum.append(shots)
        textSize(24)
        fill(0,100,0)
        text("SHOTS: "+str(shots),350,50)

def setup():
    global sz,hits,shotsnum,games
    size(600,600)
    ellipseMode(CORNER)
    sz = width/10.0
    shotsnum = []
    hits = 0
    games = 0
    
def draw():
    #frameRate(4)
    background(255)
    #create a Game and play it
    game1 = Game()
    game1.play()
    #calculate the average shots it's taking to hit the Battleship
    average_shots = int(sum(shotsnum)/float(len(shotsnum)))
    #display all the info
    fill(0,0,255)
    textSize(24)
    text("Games: "+str(games),100,50)
    text("AVERAGE: "+str(average_shots),350,80)
    #Uncomment to save screenshots:
    #saveFrame("####.png")
    
'''Average shots settles down to 24.
The book's answer is 24.'''
