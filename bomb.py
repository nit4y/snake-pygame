import game_parameters
from game_display import GameDisplay
from location import Location
import consts

class Bomb(object):
    def __init__(self, x, y, radius, timer) -> None:
        self.location = Location(x, y)
        self.radius = radius
        self.timer = timer
    
    def draw_blast_cell(self, gd, cur_x, cur_y):
        gd.draw_cell(cur_x, cur_y, consts.ORANGE)

    def draw_blast(self, gd :GameDisplay,current_radius) -> (bool):
        width = game_parameters.WIDTH #easy parameters for width and height
        height = game_parameters.HEIGHT
        #draws the current blast
        #returns True if uninteruped
        #returns False if the blast has collided and the bomb must be stopped
        is_in_bound = True #initliazing the bool
        if current_radius == 0:
            self.draw_blast_cell(gd,self.location.x, self.location.y)
        else: #if bigger than 0
            #we initalize the starting location for diamond shape movment
            cur_x = self.location.x - current_radius
            cur_y = self.location.y
            #we will use 4 loops, once for each diagonal direction
            for i in range(current_radius+1): #UP + RIGHT
                if(0 <= cur_x + i <= width) and (0 <= cur_y + i <= height):
                    self.draw_blast_cell(gd,cur_x, cur_y)
                else:
                    is_in_bound = False
            for i in range(current_radius+1): #DOWN + RIGHT
                if(0 <= cur_x + i <= width) and (0 <= cur_y - i <= height):
                    self.draw_blast_cell(gd,cur_x, cur_y)
                else:
                    is_in_bound = False
            for i in range(current_radius+1): #DOWN + LEFT
                if(0 <= cur_x - i <= width) and (0 <= cur_y - i <= height):
                    self.draw_blast_cell(gd,cur_x, cur_y)
                else:
                    is_in_bound = False
            for i in range(current_radius+1): #UP + LEFT
                if(0 <= cur_x - i <= width) and (0 <= cur_y + i <= height):
                    self.draw_blast_cell(gd,cur_x, cur_y)
                else:
                    is_in_bound = False
        #now we finished painting all cells in diamond shape
        #bool is_in_bound will remember if one of the cells exited
        return is_in_bound

    def detonate(self, gd :GameDisplay) -> (bool):
        for i in range(self.radius):
            if self.draw_blast(gd,i) == False:
                return False

    def draw_bomb(self, gd: GameDisplay):
        gd.draw_cell(self.location.x, self.location.y, consts.RED)