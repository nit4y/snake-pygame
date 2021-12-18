from snake_node import SnakeNode
from location import Location
import game_display as gd
from consts import BLACK
class Snake(object):
    def __init__(self) -> None:
        third = SnakeNode(10, 12, None, None)
        second = SnakeNode(10, 11, third, None)
        self.head = SnakeNode(10, 10, second, None)
        third.previous = second
        second.previous = self.head

        self.direction = "Up"
        self.tail = third
    
    def set_tail(self, tail):
        self.before_last.next = tail

    def set_head(self, new_head: SnakeNode) -> None:
        new_head.next = self.head
        self.head = new_head
    
    def calc_new_head_location(self) -> Location:
        if self.direction == "Left":
            return Location(self.head.location.x, self.head.location.y-1)
        elif self.direction == "Right":
            return Location(self.head.location.x, self.head.location.y+1)
        elif self.direction == "Up":
            return Location(self.head.location.x-1, self.head.location.y)
        elif self.direction == "Down":
            return Location(self.head.location.x+1, self.head.location.y)
        return None

    def movement(self):
        location = self.calc_new_head_location()
        if location != None:
            new_head = SnakeNode(location.x, location.y, None, None)
            self.head.previous = new_head
            new_head.next = self.head
            self.head = new_head

            self.tail = self.tail.previous
            self.tail.next = None
    
    def draw_snake(self, gd :gd.GameDisplay):
        runner = self.head
        while runner != None:
            gd.draw_cell(runner.location.x, runner.location.y, BLACK)
            runner = runner.next
        
            