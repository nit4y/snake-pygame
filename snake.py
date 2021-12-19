from snake_node import SnakeNode
from location import Location
import game_display as gd
from consts import BLACK
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
            return Location(self.head.location.x-1, self.head.location.y)
        elif self.direction == "Right":
            return Location(self.head.location.x+1, self.head.location.y)
        elif self.direction == "Up":
            return Location(self.head.location.x, self.head.location.y+1)
        elif self.direction == "Down":
            return Location(self.head.location.x, self.head.location.y-1)
        return None

    def movement(self):
        location = self.calc_new_head_location()
        if location != None:
            new_head = SnakeNode(location.x, location.y, None, None)
            self.head.previous = new_head
            new_head.next = self.head
            self.head = new_head

            if self.stomach == 0:
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                self.stomach = self.stomach-1
    
    def draw_snake(self, gd :gd.GameDisplay):
        runner = self.head
        while runner != None:
            gd.draw_cell(runner.location.x, runner.location.y, BLACK)
            runner = runner.next
        
    def get_locations(self):
        list_of_locations = []
        runner = self.head
        while runner.next != None:
            location_to_add = runner.location
            list_of_locations.append(location_to_add)
            runner = runner.next
        return list_of_locations
    
    def eat_apple(self):
        self.stomach+=3
