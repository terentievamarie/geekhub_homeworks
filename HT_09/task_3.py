"""
3. Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль 
      (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс 
      (файл <{username}_balance.TXT>) 
      та історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. 
      Обов'язкова перевірка введених даних (введено цифри; 
      знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз 
      при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка 
      додається в кінець файла;
      - файл з користувачами: тільки читається.
      Але якщо захочете реалізувати функціонал додавання нового користувача 
      - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - 
      буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача 
      (програма запитує ім'я/пароль). 
      Якщо вони неправильні - вивести повідомлення про це 
      і закінчити роботу (хочете - зробіть 3 спроби, 
      а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, 
      але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів 
    (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій 
"""
import csv
import json


def authenticate_user(username, password):
    with open('HT_09/task_3_files/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
    return False


def start():
    i = 0
    while i < 3:
        name = input("Please, enter your name: ")
        password = input("Please, enter your password: ")
        if authenticate_user(name, password):
            print("User authenticated!")
            menu(name)
            break
        else:
            print(f"Incorrect username or password. Remaining attempts: {2 - i}")
            i += 1


def menu(username):
    no_exit = True
    
    while no_exit:
        action = input("Please, enter your action: \n1 (Check balance) \n2 (Аccount replenishment)\n3 (Withdraw money from the account)\n4 (Exit)")
        if action == '1':
            print(f"Your balance: {get_balance(username)}")
        elif action == '2':
            print(f"Deposit: +{deposit(username)} usd")
        elif action == '3':
            print(f"Withdraw: - {withdraw(username)} usd")
        elif action == '4':
            print("You have successfully logged out.")
            no_exit = False
        else:
            print('Incorrect operation.Try again')


def get_balance(username):
    try:
        with open("HT_09/task_3_files/" + username + "_balance.txt") as file:
            content = file.read()
            if content:
                return float(content)
            else:
                return 0.0
    except FileNotFoundError:
        raise FileNotFoundError('No file with this name')


def is_count_valid(count):
    try:
        count = float(count)
        if count > 0:
            return True
        return False
    except ValueError as e:
        print(e)


def deposit(username):
    count = input("How much do you want to deposit into your account? ")
    if is_count_valid(count):
        new_balance = get_balance(username) + float(count)
        update_balance(username, new_balance)
        record_a_transaction(username, 'deposit', count)
        return count
    else:
        print("Invalid amount. Please enter a positive number.")


def withdraw(username):
    count = input("How much would you like to withdraw from your balance? ")
    if is_count_valid(count):
        current_balance = get_balance(username)
        if not float(count) > current_balance:
            new_balance = get_balance(username) - float(count)
            update_balance(username, new_balance)
            record_a_transaction(username, 'withdrawing',count)
            return count
        else:
            print("Not enough funds in the account.")
            return 0.0
    else:
        print("Invalid amount. Please enter a positive number.")


def update_balance(username, new_balance):
    try:
        with open("HT_09/task_3_files/" + username + "_balance.txt", 'w') as file:
            file.write(str(new_balance))
    except FileNotFoundError as e:
        print(e)


def read_json(username):
    try:
        with open("HT_09/task_3_files/" + username + "_transactions.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    

def record_a_transaction(username, operation, count):
    transactions = read_json(username)
    try:
        to_json = {'operation': operation, 'count': float(count)}
        transactions.append(to_json)
        with open("HT_09/task_3_files/" + username + "_transactions.json", 'w') as file:
            json.dump(transactions, file)
    except Exception as e:
        print(f"Error recording transaction: {e}")
 

if __name__ == '__main__':
    start()
 