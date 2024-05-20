from color import Color
import pygame as pg
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rowOffset = 0
        self.colOffset = 0
        self.rotation = 0
        self.color = Color.getCellColor()

    def move(self, rows, cols):
        
        self.rowOffset += rows
        self.colOffset += cols

    def getCellPosition(self):
        tiles = self.cells[self.rotation]
        movedTile = []
        for position in tiles:
            position = Position(position.row + self.rowOffset, position.col + self.colOffset)
            movedTile.append(position)
        return movedTile

    def draw(self, screen):
        tiles = self.getCellPosition()
        for tile in tiles:
            tileRect = pg.Rect(tile.col * self.cellSize + 1, tile.row * self.cellSize + 1,
                               self.cellSize - 1, self.cellSize - 1)
            pg.draw.rect(screen, self.color[self.id], tileRect)