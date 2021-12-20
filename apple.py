
from game_display import GameDisplay
from location import Location
from consts import GREEN

class Apple(object):
    """
    A class representing an apple in the game
    """
    def __init__(self, x: int, y: int, score_value :int) -> None:
        """
        initiates an Apple object instance
        :param x:
        :param y:
        :param score_value: the score the player gets when eating this apple
        """
        self.score_value = score_value
        self.location = Location(x, y)
    
    def draw(self, gd :GameDisplay) -> None:
        """
        draws the apple on the board
        :param gd: GameDisplay instance to access drawing api
        """
        gd.draw_cell(self.location.x, self.location.y, GREEN)
