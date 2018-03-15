import race
import mushers
import scrape_data

def progress_keys():
    return ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']


def finished_keys():
    return ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Total Race Time', 'Dogs In', 'rookie']


def extra_keys():
    return ['Out', 'Rest In Chkpt', 'Time Enroute', 'Previous', 'LayoverCompleted', 'Status', 'Time']


def update_iditarod(log_number):
    # extra keys originally passed to organize_data
    musher_list = scrape_data.log_data(log_number, finished_keys(), progress_keys(), extra_keys())
    
    return musher_list


def init_iditarod(log_number):
    data = scrape_data.log_data(log_number, finished_keys(), progress_keys(), extra_keys())
    race_stats = race.Race(len(data))
    # list of musher objects
    musher_objects = []
    for musher in data:
        musher_objects.append(mushers.Mushers(musher))

    return race_stats, musher_objects


if __name__ == '__main__':
    init_iditarod(1)