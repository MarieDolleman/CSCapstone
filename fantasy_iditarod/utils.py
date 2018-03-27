from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

def get_log_nums():
    url = 'http://iditarod.com/race/2018/logs/'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # table of data
    raw = soup.find_all('div', attrs={'class':'post-content'})
    raw = raw[0].text.strip()
    raw = raw.split('\n')

    all_logs = []
    for log_num in raw:
        try:
            all_logs.append(int(log_num))
        except ValueError:
            continue
    
    all_logs.reverse()
    sub_logs = int(len(all_logs)/22)
    return_logs = []
    for i, log in enumerate(all_logs[:-1]):
        if not i % sub_logs:
            return_logs.append(log)
    return_logs.append(all_logs[-1:])
    return return_logs

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
    formats = ['%d/%m %I:%M:%S', '%m/%d %I:%M:%S', '%d/%m 00:%M:%S', '%d/%m %H:%M:%S', '%m/%d %H:%M:%S',
                '%Hh %Mm', '%Hh %Mm %Ss', '%dd %Hh %Mm %Ss', ]
    for fmt in formats:
        try:
            datetime.strptime(ele, fmt)
            return True
        except ValueError:
            continue
    return False

def is_float(ele):
    if ele.isdigit():
        return False
    try:
        float(ele)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    get_log_nums()

