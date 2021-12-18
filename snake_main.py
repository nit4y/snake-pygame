import game_parameters
from snake import Snake
from bomb import Bomb
from apple import Apple
from game_display import GameDisplay

#shalom nitay


def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    snake = Snake()
    x,y = 10,10
    #THESE TWO ARE ATTEMPTS TO INITIALIZE
    #NITAY THIS IS AN APPLE TEST:
    apple_info = game_parameters.get_random_apple_data()
    apple = Apple(apple_info[0],apple_info[1],apple_info[2])
    apple.draw(gd)
    #NITAY THIS IS A BOMB TEST:
    bomb_info = game_parameters.get_random_bomb_data()
    bomb = Bomb(bomb_info[0],bomb_info[1],bomb_info[2],bomb_info[3])
    bomb.draw_bomb(gd)
    #
    gd.end_round()
    while True:
        key_clicked = gd.get_key_clicked()
        if (key_clicked == snake.direction):
            pass #this inforces that the snake can't be pulled forward
        elif (key_clicked == 'Left') and (x > 0) and (snake.direction)!= 'Right':
            x -= 1
            snake.direction = 'Left'
        elif (key_clicked == 'Right') and (x < game_parameters.WIDTH) and (snake.direction!= 'Left'):
            x += 1
            snake.direction = 'Right'
        elif (key_clicked == 'Up') and (y > 0) and (snake.direction!= 'Down'):
            y += 1
            snake.direction = 'Up'
        elif (key_clicked == 'Down') and (y < game_parameters.HEIGHT) and (snake.direction != 'Up'):
            y -= 1
            snake.direction = 'Down'
        snake.movement()
        apple.draw(gd)
        snake.draw_snake(gd)
        #FROM HERE .....
        if bomb.timer >= 1:
            bomb.draw_bomb(gd)
            bomb.timer = bomb.timer - 1
            bomb_blast_radious = bomb.radius+1
        if bomb.timer == 0 and bomb.radius >= 1:
            bomb.draw_blast(gd,bomb_blast_radious-1)
            bomb_blast_radious-=1
        #...TO HERE IS GARBAGE
        #JUST A TEST TO TRY AND MAKE BOMB EXPLODE

        gd.end_round()