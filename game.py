from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()  

    def getRandomBlock(self) -> Block:
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def moveLeft(self):
        self.currentBlock.move(0,-1)
        if self.blockInside() == False:
            self.currentBlock.move(0,1)
        
    def moveRight(self):
        self.currentBlock.move(0, 1)
        if self.blockInside() == False:
            self.currentBlock.move(0,-1)
    
    def moveDown(self):
        self.currentBlock.move(1,0)
        if self.blockInside() == False:
            self.currentBlock.move(-1,0)
            self.lockBlock()

    def lockBlock(self):
        tiles = self.currentBlock.getCellPosition()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.currentBlock.id
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()


    def rotate(self):
        self.currentBlock.rotate()

    def blockInside(self):
        tiles = self.currentBlock.getCellPosition()
        for tile in tiles:
            if self.grid.isInside(tile.row, tile.col) == False:
                return False
        return True
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.currentBlock.draw(screen)