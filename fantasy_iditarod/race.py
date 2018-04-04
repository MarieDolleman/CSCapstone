class Race():
    def __init__(self, num_mushers):
        self.__num_mushers = num_mushers
        self.check_points = []
        self.__dog_checks = []
        # If mushers drop out, the num mushers point allocation should always stay the same.

    def get_num_mushers(self):
        return self.__num_mushers

    # The 1st person in Nome gets 300 points, 2nd 200 and 3rd 100.
    def reached_Nome(self):
        if 'Nome' in self.check_points:
            return True
        else:
            return False
    
    def add_checkpoints(self, new_check_point):
        if new_check_point not in self.check_points:
            self.check_points.append(new_check_point)
        if not len(self.check_points) % 5:
            if new_check_point not in self.__dog_checks:
                self.add_dog_check(new_check_point)
            print(new_check_point)
    
    def add_dog_check(self, new_dog_check):
        self.__dog_checks.append(new_dog_check)

    def get_dog_checks(self):
        return self.__dog_checks