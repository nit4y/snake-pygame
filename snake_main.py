import game_parameters
from snake import Snake
from bomb import Bomb
from apple import Apple
from game_display import GameDisplay

#shalom nitay
#LEGAL_DIRECTIONS = ["Up","Down","Left","Right"]

def proccess_movment(snake: Snake, key_clicked: str):
    if (key_clicked == snake.direction):
        pass  # this inforces that the snake can't be pulled forward
    elif (key_clicked == 'Left') and (x > 0) and (snake.direction) != 'Right':
        snake.direction = 'Left'
    elif (key_clicked == 'Right') and (x < game_parameters.WIDTH) and (
            snake.direction != 'Left'):
        snake.direction = 'Right'
    elif (key_clicked == 'Up') and (y > 0) and (snake.direction != 'Down'):
        snake.direction = 'Up'
    elif (key_clicked == 'Down') and (y < game_parameters.HEIGHT) and (
            snake.direction != 'Up'):
        snake.direction = 'Down'

def draw_board(snake: Snake,apples: list[Apple],bomb: Bomb,gd: GameDisplay):
    snake.draw_snake(gd)
    bomb.draw_bomb(gd)
    for apple in apples:
        apple.draw(gd)

def place_single_apple(snake,bomb,apples: list):
    apple_data = game_parameters.get_random_apple_data()
    x = apple_data[0]
    y = apple_data[1]
    score = apple_data[2]
    #TODO test to see if apple spawns on snake/bomb/bomb blast/other apple
    #if passes we place the apple:
    apple = Apple(x,y,score)
    return apple
    #else we reroll apple stats and try again:
    #if the apple has no place to spawn we finish the game. the player won.


def place_apples(snake,bomb,apples: list):
    """ places missing apples, up to 3, marked by None """
    for i,apple in enumerate(apples):
        if apple is None:
            apples[i] = place_single_apple(snake,bomb,apples)
    return apples

def place_bomb(snake):
    bomb_data = game_parameters.get_random_bomb_data()
    x = bomb_data[0]
    y = bomb_data[1]
    radius = bomb_data[2]
    timer = bomb_data[3]
    #TODO test that the bomb doesn't spawn on any snake nodes
    #if passes we create the snake, else we reroll stats
    bomb = Bomb(x,y,radius,timer)
    return bomb

def check_collision(snake,apples,bomb):
    #WE CHECK: Snake self collision, touching bomb, eating apple
    #WE UPDATE: score, lengthing snake, game ending
    #start with checking snake self collision
    if has_snake_touched_himself(snake):
        end_game()
    if has_snake_eaten_apple(snake,apples):
        #TODO make snake longer, remove eaten apple
    if has_bomb_hurt_snake(snake,bomb):
        end_game()

def has_bomb_hurt_snake(snake,bomb):
    #TODO bomb_locations = bomb.get_location() -> list of bomb location/blast locationS
    #TODO we check every snake node: if in bomb_locations
    pass

def has_snake_eaten_apple(snake,apples):
    head_location = snake.head.location
    for i,apple in enumerate(apples):
        if apple.location == head_location:
            apples[i] = None #removes the apple
            return True
    return False

def has_snake_touched_himself(snake: Snake):
    head_location = snake.head.location
    runner = snake.head.next #we start from second node
    while runner.next is not None:
        if head_location == runner.location:
            return True #snake has touched himself!!
        runner = runner.next
    return False

def end_game():
    pass #TODO fix later

def main_loop(gd: GameDisplay) -> None:
    #initialzing the game:
    score = 0
    gd.show_score(score)
    snake = Snake()
    bomb = place_bomb(snake)
    apples = [None,None,None] #initiazling list
    apples = place_apples(snake,bomb,apples) #we fill it with 3 apples
    gd.end_round()
    while True:
        key_clicked = gd.get_key_clicked()
        proccess_movment(snake,key_clicked)
        snake.movement()
        #after we move the snake we make a list of all node locations
        snake_locations = snake.get_locations()
        #we test for: snake eating self, touching bomb or eating apple
        check_collision(snake_locations,apples,bomb)
        if bomb.timer == 0:
            advance_blast(bomb)
        bomb_collision(snake_locations,apples,bomb) #end game or new bomb
        apple_restock(apples)
        draw_board(snake,apples,bomb,gd)
        gd.end_round()