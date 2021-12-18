from snake_node import SnakeNode
from location import Location

class Snake(object):
    def __init__(self) -> None:
        third = SnakeNode(12, 10, None)
        second = SnakeNode(11, 10, third)
        self.head = SnakeNode(10, 10, second)
        self.dircetion = "Up"
        self.tail = third
    
    def set_tail(self, tail):
        self.before_last.next = tail

    def set_head(self, new_head: SnakeNode) -> None:
        new_head.next = self.head
        self.head = new_head
    
    def calc_new_head_location(self) -> Location:
        if self.direction == "Left":
            return Location(self.head.location.x-1, self.head.location.y)
        elif self.dircetion == "Right":
            return Location(self.head.location.x+1, self.head.location.y)
        elif self.dircetion == "Up":
            return Location(self.head.location.x, self.head.location.y-1)
        elif self.dircetion == "Down":
            return Location(self.head.location.x, self.head.location.y+1)
        return None

    def movement(self):
        location = self.calc_new_head_location()
        if location != None:
            self.head = SnakeNode(location.x, location.y, self.head)
            self.tail = self.tail.previous
            self.tail.next = None
        
            