from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

from utils import rh, is_date, is_float

def data_collect(log_number):
    url = 'http://iditarod.com/race/2018/logs/' + str(log_number) + '/'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # table of data
    raw = soup.find_all('table', attrs={'class':'current-standings'})
    return raw

def table_clean(raw):
    keys = raw[0].find_all('th')
    finished_keys = []
    for col in keys:
        finished_keys.append(col.text.strip())
    finished = raw[0].text.strip()
    finished = finished.split('\n')

    if len(raw) > 1:
        keys = raw[1].find_all('th')
        racing_keys = []
        for col in keys:
            racing_keys.append(col.text.strip())
        racing = raw[1].text.strip()
        racing = racing.split('\n')

        return [finished_keys, rh(finished), racing_keys, rh(racing)]

    return [finished_keys, rh(finished)]

def organize_data(keys, table, wanted_keys):
    windex = 0
    musher_list = []

    musher = {}
    count_spaces = 0
    for ele in table:
        # strip extra symbols, not annoyed at all
        if ' •' in ele:
            ele = ele.strip(' •')
        if ' *' in ele:
            ele = ele.strip(' *')
        
        # if its a date, continue to next
        if is_date(ele):
            continue

        # if its a float, continue to next
        if is_float(ele):
            continue

        # white space of empty values or end of row
        if ele == '':
            count_spaces += 1
            continue

        # break if scratched data
        if ele == 'Scratched' or ele == 'Withdrawn':
            return []

        if count_spaces >= 4:
            count_spaces = 0
            windex = 0
            musher = {}
        
        if '(r)' in ele:
            ele = ele.strip(' (r)')
            musher['rookie_status'] = True

        if ele.isdigit():
            ele = int(ele)

        musher[wanted_keys[windex]] = ele
        if 'Dogs' in musher.keys():
            if 'rookie_status' not in musher.keys():
                musher['rookie_status'] = False
            musher_list.append(musher)
            musher = {}
            windex = 0
            continue

        # if Pos isnt an int, its been written as a checkpoint
        if 'Pos' in musher:
            if not type(musher['Pos']) == int:
                continue

        if windex == (len(wanted_keys) - 1):
            windex = 0
        else:
            windex += 1
    return musher_list

def log_data(log_number, progress_keys):
    raw_data = data_collect(log_number)
    # returns key then corresponding table, then possibly second set of keys and table
    tables = table_clean(raw_data)
    musher_list = organize_data(tables[0], tables[1], progress_keys)
    if len(tables) > 2:
        musher_list += (organize_data(tables[2], tables[3], progress_keys))

    return musher_list

def __data_qc():
    log_number = 36 # Test log number
    progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
    # extra keys originally passed to organize_data
    musher_list = log_data(log_number, progress_keys)
    print(musher_list)

if __name__ == '__main__':
    __data_qc()
