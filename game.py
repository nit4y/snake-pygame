
from snake import Snake
from apple import Apple
from bomb import Bomb
from location import Location
from game_display import GameDisplay
import game_parameters as gp
import consts

class Game(object):
    """
    Game is a handler class
    """

    def __init__(self) -> None:
        self.score = 0
        self.init = True
        snake, bomb, apples = self.set_env()
        self.snake = snake
        self.bomb = bomb
        self.apples = apples

        self.game_over = False


    def check_snake_collisions(self) -> bool:
        """
        checks snake self collision, touching bomb, apple eating
        :return: True if snake didn't touched himself, or was hitten by a bomb, False otherwise
        """
        # WE CHECK: Snake self collision, touching bomb, eating apple
        # WE UPDATE: score, lengthing snake, game ending
        if self.snake.is_head_out_of_bounds() or self.snake.has_snake_touched_himself() or self.has_bomb_hurt_snake():
            return False
        if self.has_snake_eaten_apple():
            self.snake.eat_apple()
        return True


    def draw_board(self, gd: GameDisplay):
        self.snake.draw_snake(gd)
        for apple in self.apples:
            if apple is not None:
                apple.draw(gd)
        self.bomb.draw_bomb(gd)


    def place_single_apple(self) -> Apple:
        apple_data = gp.get_random_apple_data()
        x = apple_data[0]
        y = apple_data[1]
        score = apple_data[2]
        used_locations = {}

        while not self.is_apple_location_legal(x, y):
            used_locations[x + "," + y] = None
            if len(used_locations) >= gp.HEIGHT * gp.WIDTH:
                self.game_over = True
                return None

            apple_data = gp.get_random_apple_data()
            x = apple_data[0]
            y = apple_data[1]
            score = apple_data[2]

        # when passes we place the apple
        apple = Apple(x, y, score)
        return apple


    def is_apple_location_legal(self, x: int, y: int) -> bool:
        apple_location = Location(x,y)
        bomb_locations = self.bomb.get_locations()
        
        for bomb_location in bomb_locations:
            if bomb_location.equals(apple_location):
                return False
        
        for apple in self.apples:
            if apple is not None:
                if apple.location.equals(apple_location):
                    return False
        
        runner = self.snake.head
        while runner.next is not None:
            if runner.location.equals(apple_location):
                return False
            runner = runner.next

        return True


    def is_bomb_location_legal(self, x: int, y: int) -> bool:
        """
        checks if a given x, y location is viable as a bomb location
        :param self:
        :param x: 
        """
        if self.init:
            self.init = False
            return True

        bomb_location = Location(x,y)
        runner = self.snake.head
        while runner.next is not None:
            if runner.location.equals(bomb_location):
                return False
            runner = runner.next

        return True

    def place_apples(self):
        """ places missing apples, up to 3, marked by None """
        for i, apple in enumerate(self.apples):
            if apple is None:
                self.apples[i] = self.place_single_apple()
        return self.apples

    def place_bomb(self):
        #randomize bomb data
        bomb_data = gp.get_random_bomb_data()
        x = bomb_data[0]
        y = bomb_data[1]
        radius = bomb_data[2]
        timer = bomb_data[3]

        #if it is not good, we will keep randomizing:
        while not(self.is_bomb_location_legal(x, y)):
            bomb_data = gp.get_random_bomb_data()
            x = bomb_data[0]
            y = bomb_data[1]
            radius = bomb_data[2]
            timer = bomb_data[3]
        bomb = Bomb(x, y, radius, timer)
        return bomb

    def has_bomb_hurt_snake(self) -> bool:
        for blast_location in self.bomb.get_locations():
            runner = self.snake.head
            while runner.next is not None:
                if blast_location.equals(runner.location):
                    return True  # the snake has been bombed back to the stone age
                runner = runner.next
        return False


    def has_snake_eaten_apple(self) -> bool:
        head_location = self.snake.head.location
        for i, apple in enumerate(self.apples):
            if apple is not None and apple.location.equals(head_location):
                self.score += self.apples[i].score_value
                self.apples[i] = None  # removes the apple
                return True
        return False

    def process_movement(self, gd: GameDisplay):
        key_clicked = gd.get_key_clicked()
        self.snake.set_snake_direction(key_clicked)
        return self.snake.movement()

    def set_env(self) -> tuple[Snake, Bomb, list[Apple]]:
        snake = Snake()
        bomb = self.place_bomb()
        apples = [None, None, None]
        return (snake, bomb, apples)  

    def check_for_destroyed_apples(self):
        for loc in self.bomb.get_locations():
            for i, apple in enumerate(self.apples):
                if apple is not None:
                    if loc.equals(apple.location):
                        self.apples[i] = None
    
    def bomb_turn_processor(self) -> bool:
        self.bomb.advance_to_next_stage() #lowers timer or increaces blast
        if self.bomb.is_it_time_for_a_new_bomb():
            self.bomb = self.place_bomb() #creates a new bomb instead of current one
        if self.has_bomb_hurt_snake():
            return True
        return False
