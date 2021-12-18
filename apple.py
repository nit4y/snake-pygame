
from game_display import GameDisplay
from location import Location
from consts import GREEN
class Apple(object):
    def __init__(self, x: int, y: int, score_value :int) -> None:
        self.score_value = score_value
        self.location = Location(x, y)
    
    def draw(self, gd :GameDisplay) -> None:
        gd.draw_cell(self.location.x, self.location.y, GREEN)
