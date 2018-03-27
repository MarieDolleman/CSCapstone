from time import sleep

from get_log_number import get_log_nums
from iditarod import init_iditarod, update_iditarod
import update_insert_sql

def main():
    # Step 1: Get the first data and initialize database, all points 0
    # Step 2: Get next round of data
    # Step 3: Calculate musher scores and update
    # Step 4: Put data into database (which is then reflected in website)
    # STEP 5: Wait 5 minutes to hit Iditarod.com again
    # Step 6: Repeat through Step 2

    # STEP 1:
    race_stats, musher_objects = init_iditarod(1)
    update_insert_sql.start_race(musher_objects)

    # STEPS 2-6:
    # list of the logs we'll be using in the sim
    log_nums = get_log_nums()
    for log in log_nums[1:]:
        # STEP 2:
        updated_list = update_iditarod(log)
        # STEP 3:
        race_stats.add_checkpoints(updated_list[0]['Checkpoint'])
        # go through the updates
        for musher in updated_list:
            # search for the musher
            for obj in musher_objects:
                if obj.name == musher['Musher']:
                    obj.update(musher, race_stats.get_num_mushers(), race_stats.get_dog_checks(), race_stats.reached_Nome())
                    break
        # STEP 4:
        update_insert_sql.update_race(musher_objects)
        # STEP 5:
        sleep(5*60)

if __name__ == '__main__':
    main()