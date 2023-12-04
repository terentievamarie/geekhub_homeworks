"""
Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату
(це може бути як один день так і інтервал
- початкова і кінцева дати,
продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні
на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
"""

import requests
from datetime import datetime, timedelta

currency_options = {"1": "USD", "2": "EUR", "3": "PLN"}


def is_date_valid(date_input):
    try:
        date = datetime.strptime(date_input, "%Y.%m.%d")
        return date
    except ValueError:
        print("Invalid date format")
        return None


def is_interval_valid(date_interval):
    try:
        start_date, end_date = map(
            lambda x: x.strip(),
            date_interval.split("-")
        )
        start_date = datetime.strptime(start_date, "%Y.%m.%d")
        end_date = datetime.strptime(end_date, "%Y.%m.%d")
        delta = end_date - start_date
        dates = [start_date + timedelta(days=i) for i in range(delta.days + 1)]
        return dates
    except (ValueError, IndexError):
        print("Invalid date interval format")
        return None


def is_date_future(date_input):
    current_date = datetime.now()
    return date_input > current_date if date_input else False


def start():
    choice = input("1. Date\n2. Time interval\nPlease enter 1/2: ")

    if choice == '1':
        date_input = input('Please, enter date (YYYY.MM.DD): ')
        date = is_date_valid(date_input)
        if date and not is_date_future(date):
            currency = input('Enter currency: 1. USD\n2. EUR\n3. PLN\n: ')
            get_exchange_rate(date, currency)
        elif is_date_future(date):
            print("Entered date is in the future. Please enter a valid date.")
    elif choice == '2':
        date_interval = input(
            "Please, enter an interval (YYYY.MM.DD - YYYY.MM.DD): "
        )
        dates = is_interval_valid(date_interval)
        if dates:
            if any(is_date_future(date) for date in dates):
                print("Entered date interval contains a date from the future.")
                print("Showing exchange rates up to the future date.")
                currency = input('Enter currency: 1. USD\n2. EUR\n3. PLN\n: ')
                for date in dates:
                    if date <= datetime.now():
                        get_exchange_rate(date, currency)
                    else:
                        break
            else:
                currency = input('Enter currency: 1. USD\n2. EUR\n3. PLN\n: ')
                for date in dates:
                    get_exchange_rate(date, currency)
        else:
            print("Invalid date interval")


def get_exchange_rate(date, currency):
    base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    formatted_date = date.strftime("%Y%m%d")
    url = (
        f"{base_url}?date={formatted_date}"
        f"&valcode={currency_options[currency]}&json"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            exchange_rate = data[0].get("rate", "N/A")
            print(f"On {date.strftime('%Y-%m-%d')},", sep='')
            print(f"1 {currency_options[currency]} = {exchange_rate} UAH")
        else:
            print("No exchange rate data available ", sep='')
            print(f"for {currency_options[currency]} ", sep='')
            print(f"on {date.strftime('%Y-%m-%d')}")
    else:
        print("Error getting exchange rate  ", sep='')
        print(f"for {currency_options[currency]}", sep='')
        print(f"on {date.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    start()
