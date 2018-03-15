from urllib.request import urlopen
from bs4 import BeautifulSoup

def numeric_convert(ele):
    try:
        return int(ele)
    except ValueError:
        return ele

def data_collect(log_number):
    log_number = 677 # Test log number
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
        return [finished_keys, finished, racing_keys, racing] 

    return [finished_keys, finished]

def organize_data(keys, table, wanted_keys, extra_keys):
    kindex = 0
    musher_list = []

    musher = {}
    for ele in table:
        # skip over unwanted keys
        while keys[kindex] in extra_keys:
            kindex += 1
            if kindex >= len(keys):
                kindex = 0
        # skip over white spaces
        if ele == '':
            kindex = 0
            musher = {}
            continue
        # skip over begining keys
        elif (ele in keys):
            continue
        
        # get viable data for mushers
        elif (keys[kindex] in wanted_keys) and (keys[kindex] not in list(musher.keys())):
            # get rookie status
            if '(r)' in ele:
                ele = ele.strip('(r) ')
                musher['rookie_status'] = True
                
            elif 'rookie_status' not in musher.keys():
                musher['rookie_status'] = False

            # all other stats
            ele = numeric_convert(ele)
            musher[keys[kindex]] = ele
            kindex += 1
            # if wanted data is completed
            if len(musher) == len(wanted_keys):
                kindex = 0
                # make sure Dogs is correct key for later
                if 'Dogs In' in musher.keys():
                    musher['Dogs'] = musher.pop('Dogs In')
                musher_list.append(musher)
        # if not viable data, go through again
        else:
            kindex += 1
    return musher_list

def log_data(log_number, finished_keys, progress_keys, extra_keys):
    raw_data = data_collect(log_number)
    # returns key then corresponding table, then possibly second set of keys and table
    tables = table_clean(raw_data)
    musher_list = organize_data(tables[0], tables[1], finished_keys, extra_keys)
    if len(tables) > 1:
        musher_list += (organize_data(tables[2], tables[3], progress_keys, extra_keys))

    return musher_list

def __data_qc():
    log_number = 677 # Test log number
    progress_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Dogs', 'rookie']
    finished_keys = ['Pos', 'Musher', 'Bib', 'Checkpoint', 'Total Race Time', 'Dogs In', 'rookie']
    extra_keys = ['Out', 'Rest In Chkpt', 'Time Enroute', 'Previous', 'LayoverCompleted', 'Status', 'Time']
    # extra keys originally passed to organize_data
    print(log_data(log_number, finished_keys, progress_keys, extra_keys))

if __name__ == '__main__':
    __data_qc()
