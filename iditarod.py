import race
import mushers
import scrape_data

def main():
    log_number = 583
    # Current check point not previous checkpoint
    wanted_keys = ['Pos', 'Musher', 'Checkpoint', 'Dogs', 'Total Race Time']
    extra_keys = ['Previous', 'In', 'Out', 'LayoverCompleted']
    log = scrape_data.log_data(log_number, wanted_keys, extra_keys)
    race_stats = race.Race({'fake': 'dict'})

    def reached_Nome():
        return race_stats.in_Nome()

if __name__ == '__main__':
    main()