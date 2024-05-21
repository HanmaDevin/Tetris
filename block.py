from colors import Colors
import pygame as pg
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        movedTiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.col + self.col_offset)
            movedTiles.append(position)
        return movedTiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1


    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_position()
        for tile in tiles:
            tileRect = pg.Rect(offset_x + tile.col * self.cell_size, offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pg.draw.rect(screen, self.colors[self.id], tileRect)