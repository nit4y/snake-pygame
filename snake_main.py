from game_display import GameDisplay
from game import Game

def main_loop(gd: GameDisplay) -> None:

    # Initialzing the game:
    game = Game()
    game.place_apples()
    gd.show_score(game.score)
    game.draw_board(gd)
    game.bomb_turn_processor()
    gd.end_round()
    while True:

        if game.process_movement(gd) == False:
            game.snake.tail.previous.next = None
            break
        if not game.check_snake_collisions():
            break
        gd.show_score(game.score)

        game.bomb_turn_processor()

        if game.has_bomb_hurt_snake():
            break
        
        game.check_for_destroyed_apples()
        game.place_apples()
        game.draw_board_inside_loop_for_tests(gd)
        gd.end_round()
    game.draw_board_inside_loop_for_tests(gd)
    gd.end_round()
    