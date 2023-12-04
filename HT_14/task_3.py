"""
 http://quotes.toscrape.com/ -
 написати скрейпер для збору всієї доступної інформації
 про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
"""

import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


page_url = 'https://quotes.toscrape.com/'
csv_name = 'HT_14/quotes.csv'


def scrape_quotes(page_url):
    authors_info = []
    author_info = {}
    page_number = 1

    while True:
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all(class_='quote')

        for quote in quotes:
            text = quote.select_one('.text').text
            author = quote.select_one('.author').text
            tag = quote.select_one('.keywords').get('content')

            if author in author_info:
                birthday, born_place, description = author_info[author]
            else:
                birthday, born_place, description = scrape_authors_info(
                    urljoin(page_url, quote.select_one('a')['href']))
                author_info[author] = birthday, born_place, description

            authors_info.append(
                (text, author, born_place, birthday, description, tag,))

        print(f'Scraping page {page_number}\n')
        page_number += 1

        next_page = soup.find('li', class_='next')
        if next_page:
            page_url = urljoin(page_url, next_page.find('a')['href'])
        else:
            break

    save_to_csv(authors_info)


def scrape_authors_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    author_born_date = soup.select_one('.author-born-date').text
    author_born_location = soup.select_one(
        '.author-born-location').text.replace('in ', '')
    author_description = soup.select_one(
        '.author-description').text.replace('\n', '').strip()

    return author_born_date, author_born_location, author_description


def save_to_csv(authors_info):
    with open(csv_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(
            ['quote', 'author', 'author_born_place', 'author_born_date', 'tags', 'description'])
        csv_writer.writerows(authors_info)


if __name__ == '__main__':
    scrape_quotes(page_url)
