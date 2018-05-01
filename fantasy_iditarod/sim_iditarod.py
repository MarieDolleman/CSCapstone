from time import sleep

from utils import sim_log_nums
import update_insert_sql
import scrape_data

import mushers
import race


# Step 1: Get the first data and initialize database, all points 0
# Step 2: Get next round of data
# Step 3: Calculate musher scores
# Step 4: Update data into database (which is then reflected in website)
# STEP 5: Wait 5 minutes to hit Iditarod.com again
# Step 6: Repeat through Step 2

def progress_keys():
    return ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']

def main():
    # STEP 1:
    print('Starting Race')
    data = scrape_data.log_data(1, progress_keys())
    race_stats = race.Race(len(data))
    
    musher_objects = []
    for musher in data:
        musher_objects.append(mushers.Mushers(musher))
    update_insert_sql.start_race(musher_objects)

    # STEPS 2-6:
    # list of the logs we'll be using in the sim
    log_nums = sim_log_nums()
    print('Working log #1: 1 of %s' % (len(log_nums)+1))
    sleep(5*60)

    for log in log_nums[1:]:
        print('Working log #%s: %s of %s' % (log, (log_nums.index(log) +1), (len(log_nums) +1)))
        
        # STEP 2:
        updated_list = scrape_data.log_data(log, progress_keys())
        musher_list = []

        # STEP #3:
        for musher in updated_list:
            new_musher = mushers.Mushers(musher)
            race_stats.add_checkpoints(musher['Checkpoint'])
            new_musher.tally_points(musher, race_stats.get_num_mushers(), race_stats.get_dog_checks(), race_stats.reached_Nome())
            musher_list.append(new_musher)
        
        # STEP 4:
        update_insert_sql.update_race(musher_list)
        
        # STEP 5:
        sleep(5*60)

    print('Race Finished')
if __name__ == '__main__':
    main()