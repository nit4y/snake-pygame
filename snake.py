from snake_node import SnakeNode
from location import Location
import game_display as gd
from consts import BLACK, LEFT, RIGHT, UP, DOWN
from game_parameters import WIDTH, HEIGHT
from snake_node_head import SnakeNodeHead


class Snake(object):
    """
    Snake is a class meant to help managing the snake location on the board, and make some calculations over those location
    In addition, manages the snake movement in a convienient way
    """
    def __init__(self) -> None:
        """
        initiates a Snake instance.
        """
        third = SnakeNode(10, 8, None, None)
        second = SnakeNode(10, 9, third, None)
        self.head = SnakeNodeHead(10, 10, second)
        third.previous = second
        second.previous = self.head

        self.direction = "Up"
        self.tail = third

        self.stomach = 0


    def calc_new_head_location(self) -> Location:
        """
        calculates the new head location for each tick of the game timer
        :return: new location of the head
        """
        if self.direction == LEFT:
            return Location(self.head.location.x - 1, self.head.location.y)
        elif self.direction == RIGHT:
            return Location(self.head.location.x + 1, self.head.location.y)
        elif self.direction == UP:
            return Location(self.head.location.x, self.head.location.y + 1)
        elif self.direction == DOWN:
            return Location(self.head.location.x, self.head.location.y - 1)
        return None


    def movement(self) -> bool:
        """
        movement manager, handles movement of the snake, checks if the snake location is valid at all times
        :return: True if movement was made successfuly, False otherwise
        """
        location = self.calc_new_head_location()
        if self.is_location_illegal(location):
            return False
        if location is not None:
            new_head = SnakeNodeHead(location.x, location.y, None)
            self.head.previous = new_head
            new_head.next = self.head
            self.head = new_head

            if self.stomach == 0:
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                self.stomach = self.stomach - 1
        return True
    

    @staticmethod
    def is_location_illegal(location: Location) -> bool:
        """
        checks if a given location is legal
        :param location: gets a location that is a new location the snake is attempting to go to
        :return: True if location is illegal, False otherwise
        """
        x, y = location.x, location.y
        return not ((0 <= x < WIDTH) and (0 <= y < HEIGHT))


    def draw_snake(self, gd: gd.GameDisplay) -> None:
        """
        draws the snake to a given GameDisplay
        :param gd: a gamedisplay to draw to
        """
        runner = self.head
        while runner != None:
            gd.draw_cell(runner.location.x, runner.location.y, BLACK)
            runner = runner.next


    def get_locations(self) -> list[Location]:
        """
        gets a list of all current locations of the snake
        :return: self explanitory
        """
        list_of_locations = []
        runner = self.head
        while runner.next is not None:
            location_to_add = runner.location
            list_of_locations.append(location_to_add)
            runner = runner.next
        return list_of_locations


    def eat_apple(self) -> None:
        """
        advances the `stomach` Snake property by 3. each stomach value will eventually be translated to another node in the snake
        :return: None
        """
        self.stomach += 3


    def is_head_out_of_bounds(self) -> bool:
        """
        checks if the head of the snake is out of bounds
        :return: True if it does, False otherwise
        """
        return self.is_location_illegal(self.head.location)
    

    def set_snake_direction(self, key_clicked: str) -> None:
        """
        sets the snake location appropietly for the key the user pressed on
        :param key_clicked: the key that was clicked by the user
        """
        if (key_clicked == LEFT) and (self.direction != RIGHT):
            self.direction = LEFT
        elif (key_clicked == RIGHT) and (self.direction != LEFT):
            self.direction = RIGHT
        elif (key_clicked == UP) and (self.direction != DOWN):
            self.direction = UP
        elif (key_clicked == DOWN) and (self.direction != UP):
            self.direction = DOWN
        

    def has_snake_touched_himself(self) -> bool:
        """
        determines if the snake has touched himself or not.
        :return: True if it did, False otherwise
        """
        head_location = self.head.location
        runner = self.head.next  # we start from second node
        while runner.next is not None:
            if head_location.equals(runner.location):
                return True  # snake HAS touched himself!!
            runner = runner.next
        return False
