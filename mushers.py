import iditarod
class Mushers():
    """ Mushers class for holding all mushers data"""
    def __init__(self, musher):
        self.last_name = musher['Lname']
        self.first_name = musher['Fname']
        self.gender = musher['gender'] # Female or Male. In db its a bool
        self.num_dogs = musher['num_dogs'] # five dog checkpoints
        self.total_time = 0 # make datetime object
        self.total_points = 0
        self.pos = 0
        self.__is_rookie = musher['rookie_status']

    # call every checkpoint, first musher gets 60 points, last gets 1
    def tally_points(self, num_mushers):
        self.total_points += (num_mushers - self.pos + 1)
        if iditarod.reached_Nome():
            if self.pos <=3:
                self.total_points += 300/self.pos