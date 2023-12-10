"""
1. Викорисовуючи requests, написати скрипт, 
який буде приймати на вхід ID категорії 
із сайту https://www.sears.com і 
буде збирати всі товари із цієї категорії, 
збирати по ним всі можливі дані 
(бренд, категорія, модель, ціна, рейтинг тощо) 
і зберігати їх у CSV файл 
(наприклад, якщо категорія має ID 12345, 
то файл буде називатись 12345_products.csv)
Наприклад, категорія 
https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184
"""

import csv
import os
import requests
from fake_useragent import UserAgent


def get_data(category_id):
    user_agent = UserAgent()
    params = {
        'searchType': 'category',
        'store': 'Sears',
        'storeId': 10153,
        'catGroupId': category_id,
    }
    headers = {
        'Authorization': 'SEARS',
        'User-Agent': user_agent.random
    }
    response = requests.get('https://www.sears.com/api/sal/v3/products/search', headers=headers, params=params)
    
    return response.json()


def write_to_csv(category_id, data):
    directory = 'HT_15/task_1_files'
    if not os.path.exists(directory):
        os.makedirs(directory)

    headers = ["BrandName", "Name", "Category", "FinalPrice"]
    csv_filename = os.path.join(directory, f'{category_id}_products.csv')

    file_exists = os.path.exists(csv_filename)

    with open(csv_filename, 'a+', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        if not file_exists:
            writer.writeheader()

        for product in data.get('items', []):
            writer.writerow({
                'BrandName': product.get('brand', ''),
                'Name': product.get('name', ''),
                'Category': product.get('category', ''),
                'FinalPrice': product.get('final_price', ''),
            })


def start():
    category_id = input("Please, enter the category id: ")
    data = get_data(category_id)
    write_to_csv(category_id, data)
    print('Nice!Catched up on.')

start()