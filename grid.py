import pygame as pg
from color import Color

class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.cellSize = 30
        # generate a 2D array with zeroes and with 20 rows and 10 columns
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.colors = Color.getCellColor()

    def printGrid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end=" ")
            print()
    
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cellValue = self.grid[row][col]
                cellRect = pg.Rect(col*self.cellSize + 1, row*self.cellSize + 1, self.cellSize - 1, self.cellSize - 1)
                pg.draw.rect(screen, self.colors[cellValue], cellRect)