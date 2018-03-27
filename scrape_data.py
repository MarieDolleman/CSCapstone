from urllib.request import urlopen
from bs4 import BeautifulSoup

from datetime import datetime

def rh(table):
    '''Remove column headers from data'''
    for ele in table:
        if ' •' in ele:
            break
        elif ele.isdigit():
            break
        else:
            table = table[1:]
    return table

def is_date(ele):
    formats = ('%d/%m %I:%M:%S', '%Ih %Mm')
    for fmt in formats:
        try:
            datetime.strptime(ele, fmt)
            return True
        except ValueError:
            return False

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
    # Dumb stupid inconsistent column names
    if 'Dogs In' in keys:
        wanted_keys[wanted_keys.index('Dogs')] = 'Dogs In'
    windex = 0
    musher_list = []
    auto_skip = False

    musher = {}
    count_spaces = 0
    for ele in table:
        # if its a date, continue to next
        if is_date(ele):
            continue
        if auto_skip:
            auto_skip = False
            continue
        # skip over all key strings
        if (ele in keys):
            windex = 0
            continue
        # white space of empty values or end of row
        if ele == '':
            count_spaces += 1
            continue
        # strip extra symbols
        if ' •' in ele:
            ele = ele.strip(' •')

        if count_spaces >= 4:
            count_spaces = 0
            windex = 0
            musher = {}
        # dogs and bibs  
        if ele.isdigit():
            musher[wanted_keys[windex]] = int(ele)
            # check that all keys are in, could be finished
            if 'Dogs' in musher.keys() or 'Dogs In' in musher.keys():
                if 'Dogs In' in musher.keys():
                    musher['Dogs'] = musher.pop('Dogs In')
                musher_list.append(musher)
                musher = {}
                windex = 0
                continue
        # times, checkpoints and names. Any extras will be written over after dogs
        else:
            musher[wanted_keys[windex]] = ele
            if '(r)' in ele:
                ele = ele.strip(' (r)')
                musher['rookie_status'] = True
                    
            elif 'rookie_status' not in musher.keys():
                musher['rookie_status'] = False
        # stay on Dogs key until finished
        if wanted_keys[windex] == 'Dogs' or wanted_keys[windex] == 'Dogs In':
            windex = windex
        elif windex == (len(wanted_keys) - 1):
            windex = 0
        elif 'Pos' in musher:
            if not type(musher['Pos']) == int:
                auto_skip = True
                continue
            else:
                windex += 1
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
    log_number = 770 # Test log number
    progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
    # extra keys originally passed to organize_data
    print(log_data(log_number, progress_keys))

if __name__ == '__main__':
    __data_qc()
