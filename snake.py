from snake_node import SnakeNode
from location import Location
import game_display as gd
from consts import BLACK, LEFT, RIGHT, UP, DOWN
from game_parameters import WIDTH, HEIGHT


class Snake(object):
    def __init__(self) -> None:
        third = SnakeNode(10, 8, None, None)
        second = SnakeNode(10, 9, third, None)
        self.head = SnakeNode(10, 10, second, None)
        third.previous = second
        second.previous = self.head

        self.direction = "Up"
        self.tail = third

        self.stomach = 0

    def set_tail(self, tail):
        self.before_last.next = tail

    def set_head(self, new_head: SnakeNode) -> None:
        new_head.next = self.head
        self.head = new_head

    def calc_new_head_location(self) -> Location:
        if self.direction == "Left":
            return Location(self.head.location.x - 1, self.head.location.y)
        elif self.direction == "Right":
            return Location(self.head.location.x + 1, self.head.location.y)
        elif self.direction == "Up":
            return Location(self.head.location.x, self.head.location.y + 1)
        elif self.direction == "Down":
            return Location(self.head.location.x, self.head.location.y - 1)
        return None

    def movement(self):
        location = self.calc_new_head_location()
        if self.is_location_illlegal(location):
            return False
        if location != None:
            new_head = SnakeNode(location.x, location.y, None, None)
            self.head.previous = new_head
            new_head.next = self.head
            self.head = new_head

            if self.stomach == 0:
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                self.stomach = self.stomach - 1
        return True

    def is_location_illlegal(self,location: Location):
        x, y = location.x, location.y
        return not ((0 <= x < WIDTH) and (0 <= y < HEIGHT))

    def draw_snake(self, gd: gd.GameDisplay):
        runner = self.head
        while runner != None:
            gd.draw_cell(runner.location.x, runner.location.y, BLACK)
            runner = runner.next

    def get_locations(self):
        list_of_locations = []
        runner = self.head
        while runner.next is not None:
            location_to_add = runner.location
            list_of_locations.append(location_to_add)
            runner = runner.next
        return list_of_locations

    def eat_apple(self):
        self.stomach += 3

    def is_head_out_of_bounds(self):
        x = self.head.location.x
        y = self.head.location.y
        if not((0 <= x < WIDTH) and (0 <= y < HEIGHT)):
            return True
        else:
            return False
    
    def set_snake_direction(self, key_clicked: str):
        if (key_clicked == LEFT) and (self.direction != RIGHT):
            self.direction = LEFT
        elif (key_clicked == RIGHT) and (self.direction != LEFT):
            self.direction = RIGHT
        elif (key_clicked == UP) and (self.direction != DOWN):
            self.direction = UP
        elif (key_clicked == DOWN) and (self.direction != UP):
            self.direction = DOWN
        
    def has_snake_touched_himself(self) -> bool:
        head_location = self.head.location
        runner = self.head.next  # we start from second node
        while runner.next is not None:
            if head_location.equals(runner.location):
                return True  # snake HAS touched himself!!
            runner = runner.next
        return False

    def get_length(self):
        return len(self.get_locations())
