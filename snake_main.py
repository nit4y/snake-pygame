from typing import List
from location import Location
import game_parameters
from snake import Snake
from bomb import Bomb
from apple import Apple
from game_display import GameDisplay
import consts

# shalom nitay
#LEGAL_DIRECTIONS = ["Up","Down","Left","Right"]


def set_snake_direction(snake: Snake, key_clicked: str):
    if (key_clicked == snake.direction):
        pass  # this inforces that the snake can't be pulled forward
    elif (key_clicked == 'Left') and (snake.direction) != 'Right':
        snake.direction = 'Left'
    elif (key_clicked == 'Right') and (
            snake.direction != 'Left'):
        snake.direction = 'Right'
    elif (key_clicked == 'Up') and (snake.direction != 'Down'):
        snake.direction = 'Up'
    elif (key_clicked == 'Down') and (
            snake.direction != 'Up'):
        snake.direction = 'Down'


def draw_board(snake: Snake, apples: list[Apple], bomb: Bomb, gd: GameDisplay):
    snake.draw_snake(gd)
    for apple in apples:
        apple.draw(gd)
    draw_bomb(bomb,gd)


def place_single_apple(snake, bomb, apples: list):
    apple_data = game_parameters.get_random_apple_data()
    x = apple_data[0]
    y = apple_data[1]
    score = apple_data[2]
    # TODO test to see if apple spawns on snake/bomb/bomb blast/other apple
    # if passes we place the apple:
    apple = Apple(x, y, score)
    return apple
    # else we reroll apple stats and try again:
    # if the apple has no place to spawn we finish the game. the player won.


def place_apples(snake, bomb, apples: list):
    """ places missing apples, up to 3, marked by None """
    for i, apple in enumerate(apples):
        if apple is None:
            apples[i] = place_single_apple(snake, bomb, apples)
    return apples


def place_bomb(snake):
    bomb_data = game_parameters.get_random_bomb_data()
    x = bomb_data[0]
    y = bomb_data[1]
    radius = bomb_data[2]
    timer = bomb_data[3]
    # TODO test that the bomb doesn't spawn on any snake nodes
    # if passes we create the snake, else we reroll stats
    bomb = Bomb(x, y, radius, timer)
    return bomb


def check_collision(snake: Snake, apples: list[Apple], bomb: Bomb) -> bool:
    # WE CHECK: Snake self collision, touching bomb, eating apple
    # WE UPDATE: score, lengthing snake, game ending
    if has_snake_touched_himself(snake) or has_bomb_hurt_snake(snake, bomb.get_locations()):
        return False
    if has_snake_eaten_apple(snake, apples):
        snake.eat_apple()
    return True


def has_bomb_hurt_snake(snake: Snake, bomb_locations: list[Location]) -> bool:
    for blast_location in bomb_locations:
        runner = snake.head
        while runner.next is not None:
            if blast_location.equals(runner.location):
                return True  # the snake has been bombed back to the stone age
            runner = runner.next
    return False


def has_snake_eaten_apple(snake: Snake, apples: list[Apple]) -> bool:
    head_location = snake.head.location
    for i, apple in enumerate(apples):
        if apple.location.equals(head_location):
            apples[i] = None  # removes the apple
            return True
    return False


def has_snake_touched_himself(snake: Snake) -> bool:
    head_location = snake.head.location
    runner = snake.head.next  # we start from second node
    while runner.next is not None:
        if head_location.equals(runner.location):
            return True  # snake HAS touched himself!!
        runner = runner.next
    return False


def process_movement(gd: GameDisplay, snake: Snake):
    key_clicked = gd.get_key_clicked()
    set_snake_direction(snake, key_clicked)
    snake.movement()

def set_env() -> tuple[Snake, Bomb, list[Apple]]:
    snake = Snake()
    bomb = place_bomb(snake)
    apples = place_apples(snake, bomb, [None, None, None]) # we fill it with 3 apples
    return (snake, bomb, apples)  





def main_loop(gd: GameDisplay) -> None:
    # initialzing the game:
    score = 0
    gd.show_score(score)

    snake, bomb, apples = set_env()

    gd.end_round()
    while True:
        process_movement(gd, snake)
        # Is snake eating itself, touching bomb or eating apple
        if not check_collision(snake, apples, bomb):
            break

        #while bomb.detonate()

        #BOAZ TESTS:
        bomb.advance_to_next_stage() #lowers timer or increaces blast
        if bomb.is_it_time_for_a_new_bomb():
            bomb = place_bomb(snake) #creates a new bomb instead of current one
        if has_bomb_hurt_snake(snake,bomb.get_locations()):
            break
        place_apples(snake, bomb, apples)
        draw_board(snake, apples, bomb, gd)
        gd.end_round()
    draw_board(snake,apples,bomb,gd)
    gd.end_round()



def draw_bomb(bomb: Bomb, gd: GameDisplay):
        bomb_locations = bomb.get_locations()
        if bomb.timer > 0:
            x = bomb.location.x
            y = bomb.location.y
            gd.draw_cell(x, y, consts.RED)
        elif bomb.timer == 0:
            for current_blast_cell in bomb_locations:
                x = current_blast_cell.x
                y = current_blast_cell.y
                gd.draw_cell(x, y, consts.ORANGE)
