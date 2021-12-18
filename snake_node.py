
from location import Location

class SnakeNode(object):
    def __init__(self, x :int, y :int, next :object, previous :object) -> None:
        self.location = Location(x, y)
        self.next = next
        self.previous = previous


    def set_location(self, new_x, new_y):
        self.location = Location(new_x, new_y)