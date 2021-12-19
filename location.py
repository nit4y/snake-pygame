
from __future__ import annotations

class Location(object):
    def __init__(self, x ,y) -> None:
        self.x = x
        self.y = y
    
    def equals(self, another_location: Location):
        if self.x == another_location.x and self.y == another_location.y:
            return True
        return False
