import threading
import time
import requests
from bs4 import BeautifulSoup


urls = [
    'https://www.baidu.com',
    'https://www.taobao.com',
    'https://www.jd.com',
    'https://www.sina.com.cn',
    'https://www.163.com',
]

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'fetched {url} - {soup.title} - chars {len(response.text)}')
    return soup

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    thread = None

print('All finished')