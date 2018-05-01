class Mushers():
    '''Mushers class for holding all mushers data'''
    def __init__(self, musher):
        '''Init function, set the name, bib number, the number of dogs, points,
        whether the musher is a rookie, and the musher's current checkpoint status'''
        self.name = musher['Musher']
        self.mush_id = musher['Bib']
        self.num_dogs = musher['Dogs'] # five dog checkpoints
        self.total_points = 0
        self.pos = 0
        self.checkpoint = musher['Checkpoint']
        if musher['rookie_status']:
            self.is_rookie = 1
        else:
            self.is_rookie = 0

    def tally_points(self, musher, num_mushers, dog_check, reached_Nome):
        '''Function to tally points based on musher position and the number of dogs'''
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
        '''Return the stats of the musher object'''
        return self.num_dogs, self.total_points, self.pos, self.checkpoint, self.mush_id

    def print_musher(self):
        '''Print the stats of the musher, used for debugging purposes'''
        print(self.get_stats())
