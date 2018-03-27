import iditarod
class Mushers():
    """ Mushers class for holding all mushers data"""
    def __init__(self, musher):
        self.name = musher['Musher']
        self.mush_id = musher['Bib']
        self.num_dogs = musher['Dogs'] # five dog checkpoints
        self.total_points = 0
        self.pos = 0
        if musher['rookie_status']:
            self.is_rookie = 1
        else:
            self.is_rookie = 0

    def update(self, musher, num_mushers, dog_check, reached_Nome):
        assert(self.name == musher['Musher'])
        self.pos = musher['Pos']
        self.num_dogs = musher['Dogs']
        self.total_points += (num_mushers - self.pos + 1)
        if reached_Nome:
            if self.pos <=3:
                self.total_points += 300/self.pos

        if musher['Checkpoint'] in dog_check:
            self.total_points += self.num_dogs

    def get_stats(self):
        return self.num_dogs, self.total_points, self.pos, self.mush_id
