import game_parameters
from game_display import GameDisplay

def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    x, y = 10, 10
    while True:
        key_clicked = gd.get_key_clicked()
        if (key_clicked == 'Left') and (x > 0):
            x -= 1
        elif (key_clicked == 'Right') and (x < game_parameters.WIDTH):
            x += 1
        gd.draw_cell(x, y, "red")
        gd.end_round()