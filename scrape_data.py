from urllib.request import urlopen
from bs4 import BeautifulSoup

def data_collect(log_number):
    url = 'https://iditarod.com/race/2017/logs/' + str(log_number) + '/'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # table of data
    table = soup.find_all('table', attrs={'class':'current-standings'})

    keys = table[0].find_all('th')
    finished_keys = []
    for i, e in enumerate(keys):
        finished_keys.append(e.text.strip())
    finished = table[0].text.strip()
    finished = finished.split('\n')

    if len(table) > 1:
        keys = table[1].find_all('th')
        racing_keys = []
        for i, e in enumerate(keys):
            racing_keys[i] = e.text.strip()
        racing = table[1].text.strip()
        racing = racing.spilt('\n')
        return [racing_keys, racing, finished_keys, finished] 

    return [finished_keys, finished]

def organize_data(table, keys, wanted_keys, extra_keys):
    kindex = 0
    musher_list = []
    
    if not set(wanted_keys).issubset(table):
        raise KeyError('The data ingest process has broken. The log keys have been changed')

    mushers = {}
    for ele in table:
        if ele == '':
            continue
        if (ele in keys) or (ele not in wanted_keys):
            continue
        if '(r)' in ele:
            ele.strip('(r)')
            mushers['rookie_status'] = True
        print(keys[kindex], ele)
        mushers[keys[kindex]] = ele
        kindex += 1
        if kindex >= len(keys):
            kindex = 0
            for key in mushers:
                if key not in wanted_keys:
                    del mushers[key]
            musher_list.append(mushers)
            mushers = {}
    return musher_list

def log_data(log_number, wanted_keys, extra_keys):
    tables = data_collect(log_number)
    musher_list = organize_data(tables[0], tables[1], wanted_keys, extra_keys)
    if len(tables) > 2:
        musher_list.append(organize_data(tables[2], tables[3], wanted_keys, extra_keys))
    return musher_list

