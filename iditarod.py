import race
import mushers
import scrape_data

def main():
    log_number = 583
    # Current check point not previous checkpoint
    progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
    finished_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Total Race Time', 'Dogs In', 'rookie']
    extra_keys = ['Previous', 'Out', 'In', 'LayoverCompleted', 'Status']
    # extra keys originally passed to organize_data
    log = scrape_data.log_data(log_number, finished_keys, progress_keys, extra_keys)
    race_stats = race.Race(log[0])

    def reached_Nome():
        return race_stats.in_Nome()

if __name__ == '__main__':
    main()