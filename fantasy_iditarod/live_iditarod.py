from time import sleep

from utils import get_all_logs
import update_insert_sql
import scrape_data

import mushers
import race

def progress_keys():
    '''Return the keys we care about'''
    return ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']

def main():
    '''Assumes the Iditarod has started, and updates the table'''
    # get the available logs
    original_logs = get_all_logs()
    # if logs are empty, try again in 5
    
    while not original_logs: 
        original_logs = get_all_logs()        
        sleep(5*60)

    # ----------------------------------------------------------------------------------------
    #                                RACE HAS BEGUN BABY
    # ----------------------------------------------------------------------------------------

    # give a time out to the while loop
    timeout = 24*60*60

    data = scrape_data.log_data(1, progress_keys())
    race_stats = race.Race(len(data))
    musher_objects = []
    for musher in data:
        musher_objects.append(mushers.Mushers(musher))
    update_insert_sql.start_race(musher_objects)

    # STEPS 2-6:
    # list of the logs we'll be using in the sim
    new_logs = get_all_logs()
    print('Working log #1')
    sleep(5*60)

    lindex = 0
    while original_logs != new_logs or timeout:
        # log
        log = new_logs[lindex]

        if original_logs == new_logs:
            timeout -= 5*60
            sleep(5*60)
        # skip already used logs
        elif log in original_logs:
            lindex += 1
            continue
        
        else:
            # reset timeout
            timeout = 24*60*60
            print('Working log #%s' % log)    
            
            # STEP 2:
            updated_list = scrape_data.log_data(log, progress_keys())
            race_stats.add_checkpoints(updated_list[0]['Checkpoint'])
            musher_list = []
            # STEP #3:
            for musher in updated_list:
                new_musher = mushers.Mushers(musher)
                new_musher.tally_points(musher, race_stats.get_num_mushers(), race_stats.get_dog_checks(), race_stats.reached_Nome())
                musher_list.append(new_musher)
            # STEP 4:
            update_insert_sql.update_race(musher_list)
            # STEP 5:
            sleep(5*60)
            
            # add used log to original
            original_logs.append(log)
            # add any new logs to the new_log list
            added_logs = get_all_logs()
            for l in added_logs:
                if l not in new_logs:
                    new_logs.append(l)
            lindex += 1
    
    # wait three weeks before deleting the table
    sleep(60*60*24*7*3)
    update_insert_sql.clear_table()
