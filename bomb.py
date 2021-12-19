import bomb
import game_parameters
from game_display import GameDisplay
from location import Location
import consts


class Bomb(object):
    def __init__(self, x, y, radius, timer) -> None:
        self.location = Location(x, y)
        self.radius = radius
        self.timer = timer
        self.blast_length = 0

    def draw_blast_cell(self, gd, cur_x, cur_y):
        gd.draw_cell(cur_x, cur_y, consts.ORANGE)

    def draw_blast(self, gd: GameDisplay, current_radius) -> (bool):
        width = game_parameters.WIDTH  # easy parameters for width and height
        height = game_parameters.HEIGHT
        # draws the current blast
        # returns True if uninteruped
        # returns False if the blast has collided and the bomb must be stopped
        is_in_bound = True  # initliazing the bool
        if current_radius == 0:
            self.draw_blast_cell(gd, self.location.x, self.location.y)
        else:  # if bigger than 0
            # we initalize the starting location for diamond shape movment
            cur_x = self.location.x - current_radius
            cur_y = self.location.y
            # we will use 4 loops, once for each diagonal direction
            for i in range(current_radius + 1):  # UP + RIGHT
                if (0 <= cur_x + i <= width) and (0 <= cur_y + i <= height):
                    self.draw_blast_cell(gd, cur_x, cur_y)
                else:
                    is_in_bound = False
            for i in range(current_radius + 1):  # DOWN + RIGHT
                if (0 <= cur_x + i <= width) and (0 <= cur_y - i <= height):
                    self.draw_blast_cell(gd, cur_x, cur_y)
                else:
                    is_in_bound = False
            for i in range(current_radius + 1):  # DOWN + LEFT
                if (0 <= cur_x - i <= width) and (0 <= cur_y - i <= height):
                    self.draw_blast_cell(gd, cur_x, cur_y)
                else:
                    is_in_bound = False
            for i in range(current_radius + 1):  # UP + LEFT
                if (0 <= cur_x - i <= width) and (0 <= cur_y + i <= height):
                    self.draw_blast_cell(gd, cur_x, cur_y)
                else:
                    is_in_bound = False
        # now we finished painting all cells in diamond shape
        # bool is_in_bound will remember if one of the cells exited
        return is_in_bound

    def detonate(self, gd: GameDisplay) -> (bool):
        # for i in range(self.radius):
        #    if self.draw_blast(gd,i) == False:
        #        return False
        if self.timer == 0:
            self.draw_blast()
            self.blast_length + 1
            if self.blast_length > self.radius:
                return True
        else:
            self.timer = self.timer - 1
        return False

    def tick_timer(self):
        self.timer = self.timer - 1





#BOAZ :


    def draw_bomb(self, gd: GameDisplay):
        bomb_locations = self.get_locations()
        if self.timer > 0:
            x = self.location.x
            y = self.location.y
            gd.draw_cell(x, y, consts.RED)
        elif self.timer == 0:
            for current_blast_cell in bomb_locations:
                x = current_blast_cell.x
                y = current_blast_cell.y
                gd.draw_cell(x, y, consts.ORANGE)

    def advance_to_next_stage(self):
        if self.timer == 0:
            self.blast_length = self.blast_length + 1
        else:
            self.timer = self.timer - 1

    def is_it_time_for_a_new_bomb(self):
        return self.blast_length == self.radius

    def get_locations(self):
        if self.timer > 0:
            return [self.location]
        else:
            list_of_all_locations = []
            width = game_parameters.WIDTH  # easy parameters for width and height
            height = game_parameters.HEIGHT
            # draws the current blast
            # returns True if uninteruped
            # returns False if the blast has collided and the bomb must be stopped
            if self.blast_length == 0:
                return [self.location]
            else:  # if bigger than 0
                # we initalize the starting location for diamond shape movment
                cur_x = self.location.x - self.blast_length
                cur_y = self.location.y
                # we will use 4 loops, once for each diagonal direction
                for i in range(1,self.blast_length+1):  # UP + RIGHT
                    if (0 <= cur_x < width) and (
                            0 <= cur_y < height):
                        list_of_all_locations.append(Location(cur_x, cur_y))
                    cur_x += 1
                    cur_y += 1

                for i in range(1,self.blast_length+1):  # DOWN + RIGHT
                    if (0 <= cur_x < width) and (
                            0 <= cur_y < height):
                        list_of_all_locations.append(Location(cur_x, cur_y))
                    cur_x += 1
                    cur_y -= 1

                for i in range(1,self.blast_length+1):  # DOWN + LEFT
                    if (0 <= cur_x < width) and (
                            0 <= cur_y < height):
                        list_of_all_locations.append(Location(cur_x, cur_y))
                    cur_x -= 1
                    cur_y -= 1

                for i in range(1,self.blast_length+1):  # UP + LEFT
                    if (0 <= cur_x < width) and (
                            0 <= cur_y < height):
                        list_of_all_locations.append(Location(cur_x, cur_y))
                    cur_x -= 1
                    cur_y += 1

            # now we finished painting all cells in diamond shape
            return list_of_all_locations
