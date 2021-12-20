from game_display import GameDisplay
from game import Game

def main_loop(gd: GameDisplay) -> None:

    # Initialzing the game:
    game = Game()
    gd.show_score(game.score)
    gd.end_round()

    while True:
        if game.process_movement(gd) == False:
            break
        if not game.check_snake_collisions():
            break
        gd.show_score(game.score)

        if game.bomb_turn_processor():
            break
        
        game.check_for_destroyed_apples()
        game.place_apples()
        game.draw_board(gd)
        gd.end_round()

    game.draw_board(gd)
    gd.end_round()
    