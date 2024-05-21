import pygame as pg
import sys
from game import Game


def main():
    pg.init()

    DIMENSIONS = (300, 600) 
    DARK_BLUE = (44, 44, 127)

    screen = pg.display.set_mode(DIMENSIONS)
    # Title of the Game
    pg.display.set_caption("Tetris")
    clock = pg.time.Clock()
    running = True

    game = Game()
    GAME_UPDATE = pg.USEREVENT
    pg.time.set_timer(GAME_UPDATE, 200)

    while(running):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
           
            if event.type == pg.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.reset()
                # movement
                if event.key == pg.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pg.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pg.K_DOWN and game.game_over == False:
                    game.move_down()
                if event.key == pg.K_UP and game.game_over == False:
                    game.rotate()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down() 
        # Draw the Game
        screen.fill(DARK_BLUE)
        game.draw(screen)
        
        pg.display.update()
        clock.tick(60)

if (__name__ == "__main__"):
    main()