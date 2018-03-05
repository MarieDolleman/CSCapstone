from urllib.request import urlopen
from bs4 import BeautifulSoup

def numeric_convert(ele):
    try:
        return int(ele)
    except ValueError:
        return ele

def data_collect(log_number):
    url = 'https://iditarod.com/race/2017/logs/' + str(log_number) + '/'
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

    mushers = {}
    for ele in table:
        while keys[kindex] in extra_keys:
            kindex += 1
            if kindex >= len(keys):
                kindex = 0
        if ele == '':
            kindex = 0
            mushers = {}
            continue
        elif (ele in keys):
            continue
        
        elif (keys[kindex] in wanted_keys) and (keys[kindex] not in list(mushers.keys())):
            if '(r)' in ele:
                ele = ele.strip('(r) ')
                mushers['rookie_status'] = True
                
            elif 'rookie_status' not in mushers.keys():
                mushers['rookie_status'] = False

            ele = numeric_convert(ele)
            mushers[keys[kindex]] = ele
            kindex += 1
            if len(mushers) == len(wanted_keys):
                kindex = 0
                musher_list.append(mushers)
        else:
            kindex += 1
    return musher_list

def log_data(log_number, finished_keys, progress_keys, extra_keys):
    raw_data = data_collect(log_number)
    # returns key then corresponding table, then possibly second set of keys and table
    tables = table_clean(raw_data)
    musher_list = organize_data(tables[0], tables[1], finished_keys, extra_keys)
    if len(tables) > 2:
        musher_list.append(organize_data(tables[2], tables[3], progress_keys, extra_keys))
    return musher_list

