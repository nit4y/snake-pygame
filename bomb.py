
from game_display import GameDisplay
from location import Location


class Bomb(object):
    def __init__(self, x, y, radius, timer) -> None:
        self.location = Location(x, y)
        self.radius = radius
        self.timer = timer
    
    def draw_blast(self, gd :GameDisplay):
        gd.draw_cell(self.x)

    def detonate(self, gd :GameDisplay):
        for i in range(self.radius):
