from datetime import datetime, timedelta
from time import sleep

import race
import mushers
import scrape_data

def main():
    log_number = 583
    # Current check point not previous checkpoint
    progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
    finished_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Total Race Time', 'Dogs In', 'rookie']
    extra_keys = ['Out', 'Rest In Chkpt', 'Time Enroute', 'Previous', 'LayoverCompleted', 'Status', 'Time']
    # extra keys originally passed to organize_data
    scrape_data.log_data(log_number, finished_keys, progress_keys, extra_keys)
    #race_stats = race.Race(log[0])

    #def reached_Nome():
        #return race_stats.in_Nome()

def call_data():
    for i in range(0, 61):
        print('Hello')
        sleep(10)

if __name__ == '__main__':
    main()