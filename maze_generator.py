import pygame
import sys
from random import randint

WIDTH = 1000
HEIGHT = 1000

cell_size = 20

cols =  WIDTH/cell_size
rows =  HEIGHT/cell_size

grid = []

screen = pygame.display.set_mode((WIDTH + cols, HEIGHT + rows))
clock = pygame.time.Clock()

class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False


    def checkNeighbors(self, grid):
        self.neighbors = []

        try:
            top  = grid[self.i][self.j - 1]
            if (top.i >= 0 and top.i <= cols - 1):
                if(top.j >= 0 and top.j <= rows - 1):
                    if (not top.visited):
                        self.neighbors.append(top)
                    else:
                        pass
                else:
                    pass
            else:
                pass

        except:
            pass


        try:
            right  = grid[self.i + 1][self.j]
            if (right.i >= 0 and right.i <= cols):
                if(right.j >= 0 and right.j <= rows):
                    if (not right.visited):
                        self.neighbors.append(right)
                    else:
                        pass
                else:
                    pass
            else:
                pass

        except:
            pass

        try:
            bottom = grid[self.i][self.j + 1]
            if (bottom.i >= 0 and bottom.i <= cols):
                if(bottom.j >= 0 and bottom.j <= rows):
                    if (not bottom.visited):
                        self.neighbors.append(bottom)
                    else:
                        pass
                else:
                    pass
            else:
                pass

        except:
            pass

        try:
            left   = grid[self.i - 1][self.j]
            if (left.i >= 0 and left.i <= cols):
                if(left.j >= 0 and left.j <= rows):
                    if (not left.visited):
                        self.neighbors.append(left)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        except:
            pass



        if (len(self.neighbors) >= 0):
            try:
                r = randint(0,len(self.neighbors)- 1)
                return self.neighbors[r]
            except:
                return False

    def show(self, surface):
        self.surface = surface
        x = self.i * (cell_size + 1)
        y = self.j * (cell_size + 1)

        if (self.walls[0]):
            pygame.draw.line(self.surface, (pygame.Color('black')),  (x,y)                          ,   (x + cell_size, y)             )

        if (self.walls[1]):
            pygame.draw.line(self.surface, (pygame.Color('black')),  (x + cell_size, y)             ,   (x + cell_size, y + cell_size) )

        if (self.walls[2]):
            pygame.draw.line(self.surface, (pygame.Color('black')),  (x + cell_size, y + cell_size) ,   (x, y + cell_size)             )

        if (self.walls[3]):
            pygame.draw.line(self.surface, (pygame.Color('black')),  (x, y + cell_size)             ,   (x , y)                        )

        if self.visited:
            pygame.draw.rect(self.surface, (pygame.Color('purple')), (x, y, cell_size, cell_size))

def createDataStructure():
    for i in range(cols):
        new = []
        for j in range(rows):
            new.append(Cell(i,j))
        grid.append(new)

def draw():
    screen.fill(pygame.Color('white'))

    for i in range(cols):
        for j in range(rows):
            grid[i][j].show(screen)


def update(atual):
    atual.visited = True

    next = atual.checkNeighbors(grid)

    if next:
        next.visited = True
        atual = next

    return atual

createDataStructure()
pygame.init()

current = grid[0][0]


while 1 :
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    current = update(current)
    draw()
    pygame.display.update()
