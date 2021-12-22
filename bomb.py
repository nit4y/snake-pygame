import bomb
from game_parameters import WIDTH, HEIGHT
from game_display import GameDisplay
from location import Location
import consts



class Bomb(object):
    def __init__(self, x, y, radius, timer) -> None:
        """
        :param x: horizontal value of the bomb
        :param y: vertical value of the bomb
        :param radius: the maximum length of the bomb blast
        :param timer: how many loops of the main_loop it will take for the blast to appear
        :return: None
        """
        self.location = Location(x, y)
        self.radius = radius
        #print("RADIUS:  " + str(radius))
        self.timer = timer
        self.blast_length = 0

    def tick_timer(self):
        """
        lowers the timer before blast
        """
        self.timer = self.timer - 1

    def advance_to_next_stage(self):
        """
        if the timer is not 0 it will cause one tick of the bomb
        if the timer is 0 it will update blast_length and make it reach further
        """
        if self.timer <= 0:
            self.blast_length = self.blast_length + 1
        self.tick_timer()

    def is_it_time_for_a_new_bomb(self):
        """
        a test to see if the blast_length has passed the maximum blast radius
        for current bomb
        """
        return self.blast_length > self.radius

    def get_locations(self):
        """
        :return: a list of all locations currently affected by the bomb:
        if it hasn't exploded yet it will return the bomb's location
        if it has exploded it will return the current cells affected by the blast
        as long as they are legal values
        """
        if self.timer >= 0:
            return [self.location]
        else:
            list_of_all_locations = []
            # draws the current blast
            # returns True if uninteruped
            # returns False if the blast has collided and the bomb must be stopped

            # if bigger than 0
            # we initalize the starting location for diamond shape movment
            cur_x = self.location.x - self.blast_length
            cur_y = self.location.y
            # we will use 4 loops, once for each diagonal direction
            for _ in range(self.blast_length):  # UP + RIGHT
                if (0 <= cur_x < WIDTH) and (0 <= cur_y < HEIGHT):
                    list_of_all_locations.append(Location(cur_x, cur_y))
                cur_x += 1
                cur_y += 1

            for _ in range(self.blast_length):  # DOWN + RIGHT
                if (0 <= cur_x < WIDTH) and (0 <= cur_y < HEIGHT):
                    list_of_all_locations.append(Location(cur_x, cur_y))
                cur_x += 1
                cur_y -= 1

            for _ in range(self.blast_length):  # DOWN + LEFT
                if (0 <= cur_x < WIDTH) and (0 <= cur_y < HEIGHT):
                    list_of_all_locations.append(Location(cur_x, cur_y))
                cur_x -= 1
                cur_y -= 1

            for _ in range(self.blast_length):  # UP + LEFT
                if (0 <= cur_x < WIDTH) and (
                        0 <= cur_y < HEIGHT):
                    list_of_all_locations.append(Location(cur_x, cur_y))
                cur_x -= 1
                cur_y += 1

            # now we finished painting all cells in diamond shape
            return list_of_all_locations

    def get_size(self) -> int:
        """
        :return: int value of the amount of cells currently taken by the bomb
        """
        return len(self.get_locations())

    def draw_bomb(self, gd: GameDisplay):
        """
        :param gd: the GameDisplay object we run the game on
        this function draws the bomb if the timer is not 0
        or draws the blast if the bomb has reached 0
        """
        bomb_locations = self.get_locations()
        if self.timer > 0:
            x = self.location.x
            y = self.location.y
            gd.draw_cell(x, y, consts.RED)
        elif self.timer == 0:
            x = self.location.x
            y = self.location.y
            gd.draw_cell(x, y, consts.ORANGE)
        else:
            #print(
            #    "cell is ORANGE but blast_legnth is " + str(self.blast_length))
            for current_blast_cell in bomb_locations:
                x = current_blast_cell.x
                y = current_blast_cell.y
                gd.draw_cell(x, y, consts.ORANGE)
