
from __future__ import annotations

class Location(object):
    """
    A blob class to store an X, Y pair
    """
    def __init__(self, x ,y) -> None:
        """
        initiates a Location instance
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
    

    def equals(self, another_location: Location) -> bool:
        """
        checks if a location is equal to another_location
        :param another_location: the location to compare to
        :return: True if it does, False otherwise
        """
        if self.x == another_location.x and self.y == another_location.y:
            return True
        return False
