"""
 http://quotes.toscrape.com/ -
 написати скрейпер для збору всієї доступної інформації
 про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
"""

import requests
from bs4 import BeautifulSoup
import csv


def scrape_quotes(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []

    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        quotes.append({
            'Text': text, 'Author': author, 'Tags': ', '.join(tags)
        })

    return quotes


def save_to_csv(quotes, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Text', 'Author', 'Tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(quotes)


def main():
    base_url = 'http://quotes.toscrape.com/page/'
    num_pages = 10

    all_quotes = []

    for page_num in range(1, num_pages + 1):
        page_url = f'{base_url}{page_num}/'
        quotes = scrape_quotes(page_url)
        all_quotes.extend(quotes)

    save_to_csv(all_quotes, 'quotes.csv')
    print(f'Successfully scraped {len(all_quotes)} quotes and saved')


if __name__ == "__main__":
    main()
 