import pygame as pg
import sys
from game import Game
from colors import Colors

def main():
    pg.init()
    
    title_font =pg.font.Font(None, 40)
    # score text stuff
    score_surface = title_font.render("Score:", True, Colors.white)
    score_position = (365, 20, 50, 50)
    score_rect = pg.Rect(320, 55, 170, 60)
    # next text stuff
    next_surface = title_font.render("Next:", True, Colors.white)
    next_position = (375, 180, 50, 50)
    next_rect = pg.Rect(320, 215, 170, 180)
    # game over message stuff
    game_over_surface = title_font.render("GAME OVER", True, Colors.white)
    game_over_position = (320, 450, 50, 50)

    DIMENSIONS = (500, 620) 

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
                    game.update_score(0, 1)
                if event.key == pg.K_UP and game.game_over == False:
                    game.rotate()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down() 
                game.update_score(0, 1)
        # Draw the Game
        score_value_surface = title_font.render(str(game.score), True, Colors.white)

        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, score_position)
        screen.blit(next_surface, next_position)

        if game.game_over == True:
            screen.blit(game_over_surface, game_over_position)

        pg.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        # center the score in the score textfield
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
        pg.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)
        
        pg.display.update()
        clock.tick(60)

if (__name__ == "__main__"):
    main()