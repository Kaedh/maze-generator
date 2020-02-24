import pygame, sys, random

WIDTH  = 600
HEIGHT = 600

cell_size = 15

cols = WIDTH/cell_size
rows = HEIGHT/cell_size

screen = pygame.display.set_mode((WIDTH + 2, HEIGHT + 2))
clock = pygame.time.Clock()
pygame.display.set_caption("Maze Generator")

grid  = []
stack = []


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.visited = False
        self.walls = [True, True, True, True]
        self.highlight = False

    def pick_a_random_element(self, list):
        if len(list) > 0:
            return random.choice(list)
        else:
            return None

    def get_neighbors(self, maze_grid):
        self.neighbors = []

        #Check if is the top neighbor a valid one
        if self.i >= 0 and self.j - 1 >= 0 and self.i < cols and self.j - 1 < rows:
            top = maze_grid[self.i][self.j - 1]
            if top.visited == False:
                self.neighbors.append(top)

        #Check if is the right neighbor a valid one
        if self.i + 1 >= 0 and self.j >= 0 and self.i + 1 < cols and self.j < rows:
            right = maze_grid[self.i + 1][self.j]
            if right.visited == False:
                self.neighbors.append(right)

        #Check if is the bottom neighbor a valid one
        if self.i >= 0 and self.j + 1 >= 0 and self.i < cols and self.j + 1 < rows:
            bottom = maze_grid[self.i][self.j + 1]
            if bottom.visited == False:
                self.neighbors.append(bottom)

        #Check if is the left neighbor a valid one
        if self.i - 1 >= 0 and self.j >= 0 and self.i - 1 < cols and self.j < rows:
            left = maze_grid[self.i - 1][self.j]
            if left.visited == False:
                self.neighbors.append(left)

        pick_one = self.pick_a_random_element(self.neighbors)

        if pick_one:
            return pick_one
        else:
            pass

    def show(self, surface):
        self.surface = surface

        x = self.i * cell_size
        y = self.j * cell_size

        if self.visited:
            pygame.draw.rect(self.surface, (pygame.Color('white')), (x, y, cell_size, cell_size))

        if self.highlight:
            pygame.draw.rect(self.surface, (pygame.Color('black')), (x, y, cell_size, cell_size))

        if self.walls[0]:
            pygame.draw.line(self.surface, (pygame.Color('black')), (x,y), (x + cell_size, y),3)

        if self.walls[1]:
            pygame.draw.line(self.surface, (pygame.Color('black')), (x + cell_size, y), (x + cell_size, y + cell_size),3)

        if self.walls[2]:
            pygame.draw.line(self.surface, (pygame.Color('black')), (x + cell_size, y + cell_size), (x, y + cell_size),3)

        if self.walls[3]:
            pygame.draw.line(self.surface, (pygame.Color('black')), (x, y + cell_size), (x , y),3)


def createDataStructure():
    for i in range(cols):
        new = []
        for j in range(rows):
            new.append(Cell(i,j))
        grid.append(new)


def draw():
    screen.fill(pygame.Color('grey'))

    for i in range(cols):
        for j in range(rows):
            grid[i][j].show(screen)


def remove_wall(current, next):
    x = current.i  - next.i

    if x == 1:
        current.walls[3] = False
        next.walls[1] = False

    else:
        if x == -1:
            current.walls[1] = False
            next.walls[3] = False


    y = current.j  - next.j

    if y == 1:
        current.walls[0] = False
        next.walls[2] = False

    else:
        if y == -1:
            current.walls[2] = False
            next.walls[0] = False


def get_next_cell(current_cell):
    if current_cell:
        current_cell.visited = True
        current_cell.highlight = False

        next = current_cell.get_neighbors(grid)

        if next:
            next.visited = True
            stack.append(current_cell)
            remove_wall(current_cell, next)
            return next

        else:
            if len(stack) > 0:
                current_cell = stack.pop()
                return current_cell

            else:
                return current_cell


def main():
    createDataStructure()

    pygame.init()
    current = grid[0][0]

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        draw()
        current = get_next_cell(current)
        current.highlight = True
        pygame.display.update()


if __name__ == '__main__':
    main()
