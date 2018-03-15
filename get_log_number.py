from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_log_num():
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

if __name__ == '__main__':
    get_log_num()

