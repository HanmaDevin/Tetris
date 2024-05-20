import pygame as pg
import sys
from game import Game

pg.init()

DIMENSIONS = (300, 600) 
DARK_BLUE = (44, 44, 127)

screen = pg.display.set_mode(DIMENSIONS)
# Title of the Game
pg.display.set_caption("Tetris")
clock = pg.time.Clock()
running = True

game = Game()

def main():

    while(running):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        # Draw the Game
        screen.fill(DARK_BLUE)
        game.draw(screen)
        pg.display.update()
        clock.tick(60)