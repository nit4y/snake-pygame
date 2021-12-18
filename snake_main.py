import game_parameters
from game_display import GameDisplay
from snake import Snake
#shalom nitay


def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    x, y = 10, 10
    snake = Snake()
    while True:

        key_clicked = gd.get_key_clicked()
        if (key_clicked == 'Left') and (x > 0):
            #x -= 1
            snake.movement()
        elif (key_clicked == 'Right') and (x < game_parameters.WIDTH):
            x += 1
        
        
        snake.draw_snake(gd)
        #gd.draw_cell(x, y, "red")
        gd.end_round()