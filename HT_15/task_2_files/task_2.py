"""
2. Викорисовуючи requests, заходите на ось цей сайт 
"https://www.expireddomains.net/deleted-domains/" 
(з ним будьте обережні), вибираєте будь-яку на 
ваш вибір доменну зону і парсите список  доменів - 
їх там буде десятки тисяч (звичайно ураховуючи пагінацію). 
Всі отримані значення зберігти в CSV файл.
"""

import csv
import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
import os


def generate_random_user_agent():
    ua = UserAgent()
    return ua.random


def random_headers():
    headers = {
            'User-Agent': generate_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Ch-UA': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'Sec-Ch-UA-Mobile': '?0',
            'Sec-Ch-UA-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }
    return headers


def parse_headers(url):
    response = requests.get(url, headers=random_headers())
    soup = BeautifulSoup(response.text, 'lxml')

    headers = soup.find_all('th')
    headers_titles = [title.a.text for title in headers]

    return headers_titles


def parse_rows(url):
    response = requests.get(url, headers=random_headers())
    soup = BeautifulSoup(response.text, 'lxml')

    all_rows = soup.find('tbody').find_all('tr')
    rows = []

    for row in all_rows:
        current_row = row.find_all('td')
        row_data = []

        for el in current_row:
            row_data.append(el.a.text if el.a else el.text)

        rows.append(row_data)
    return rows


def get_all_domains_info(url):
    headers = parse_headers(url)
    rows = parse_rows(url)
    domains = []
    domains.append(headers)
    domains.append(rows)
    for page in [i for i in range(25, 326, 25)]:
        time.sleep(5)
        next_page = f'{url}?start={page}#listing'
        next_rows = parse_rows(next_page)
        domains.append(next_rows)

    return domains


def write_to_csv(filename='HT_15/task_2_files/domains_data.csv'):
    url = "https://www.expireddomains.net/expired-domains/?ftlds[]=3"
    file_exists = os.path.exists(filename)
    data = get_all_domains_info(url)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        if not file_exists:
            csvwriter.writerow(data[0])

        for page_data in data[1:]:
            print('Processing...')
            for idx, row in enumerate(page_data, 1):
                csvwriter.writerow(row)
                print(f'Processed {idx} rows')


write_to_csv()
 