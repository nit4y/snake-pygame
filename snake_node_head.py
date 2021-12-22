
from location import Location

class SnakeNodeHead(object):
    """
    A node in the snake which is a linked list. See snake.py.
    """
    def __init__(self, x :int, y :int, next :object) -> None:
        """
        initiates a SnakeNode instance
        :param x:
        :param y:
        :param next: the next node in linked list chain
        :param previous: the previous node in linked list chain
        """
        self.location = Location(x, y)
        self.next = next
