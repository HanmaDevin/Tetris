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
    
    def moveRight(self):
        self.currentBlock.move(0,1)
    
    def moveDown(self):
        self.currentBlock.move(1,0)
    
    def moveUp(self):
        self.currentBlock.move(-1,0)
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.currentBlock.draw(screen)