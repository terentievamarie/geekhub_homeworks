"""
HT #10
Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних. 
    Більше ніяких файлів. Якщо в попередньому завданні 
    ви добре продумали структуру програми 
    то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити новго користувача 
    (при створенні новго користувача, перевіряється відповідність логіну 
    і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці (базі) з користувачами має бути створений 
    унікальний користувач-інкасатор, який матиме розширені можливості 
    (домовимось, що логін/пароль будуть 
    admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена. 
    Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися 
    їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти 
    на рахунок лише сумму кратну мінімальному 
    номіналу що підтримує банкомат. 
    В іншому випадку - повернути "здачу" 
    (наприклад при поклажі 1005 --> повернути 5). 
    Але це не має впливати на баланс/кількість купюр банкомату, 
    лише збільшуєтсья баланс користувача 
    (моделюємо наявність двох незалежних касет в банкоматі 
    - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, 
    але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції 
    - вивести повідомлення з причиною 
    (не вірний логін/пароль, недостатньо коштів на раунку, 
    неможливо видати суму наявними купюрами тощо.)
"""
from pathlib import Path
import os
import sqlite3 as sl

BASE_DIR = Path(__file__).parent
DB_DIR = os.path.join(BASE_DIR, 'ATM.db')


def login(login, password):
    conn = sl.connect(DB_DIR)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE login = ? AND password = ?', (login, password))
    user_data = cursor.fetchone()

    conn.commit()
    conn.close()

    if user_data is not None:
        return True
    return False


def is_valid_user(username, password):
    if not password[0].isupper():
        print('First letter must be uppercase')
        return False

    if len(username) < 5 or len(password) < 12:
        print('Incorrect lenght of username or password')
        return False

    special_symbols = ['!', '#', '.']

    if not any(char in special_symbols for char in password):
        print("Password must contain at least one special symbol from {! # .}")
        return False
    return True


def create_user():
    username = input("Create your login: ")
    password = input('Create a password: ')
    if is_valid_user(username, password):
        conn = sl.connect(DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (login, password, is_admin)
            VALUES (?, ?, ?)
        """, (username, password, 0))

        cursor.execute("""
            INSERT INTO users_balance (user_id, balance)
            VALUES ((SELECT user_id FROM users WHERE login = ?), 0)
        """, (username,))

        conn.commit()
        conn.close()
        print("User created successfully.")
        return True
    else:
        print("User creation failed. Please check the validity of your username and password.")
        return False


def return_user_id(username):
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT user_id FROM users WHERE login = ?', (username,))
            data = cursor.fetchone()
            if data is not None:
                return data[0]
            else:
                return None
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None
    

def create_db():
    conn = sl.connect(DB_DIR)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        is_admin INTEGER DEFAULT 0);
    """)

    cursor.execute("""
        INSERT INTO users (login, password, is_admin)
        VALUES('admin', 'admin', 1)
        ON CONFLICT(login) DO NOTHING;
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users_balance(
        balance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        balance REAL,
        FOREIGN KEY (user_id) REFERENCES users(user_id));
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users_transactions(
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        transaction_name TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id));
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ATM_balance(
        nominal INTEGER PRIMARY KEY NOT NULL,
        count INTEGER DEFAULT 0);
    """)

    cursor.execute("""
        INSERT INTO ATM_balance (nominal, count)
        VALUES(10, 15)
        ON CONFLICT(nominal) DO NOTHING;
    """)

    cursor.execute("""
        INSERT INTO ATM_balance (nominal, count)
        VALUES(20, 15)
        ON CONFLICT(nominal) DO NOTHING;
    """)

    cursor.execute("""
        INSERT INTO ATM_balance (nominal, count)
        VALUES(50, 15)
        ON CONFLICT(nominal) DO NOTHING;
    """)

    cursor.execute("""
        INSERT INTO ATM_balance (nominal, count)
        VALUES(100, 15)
        ON CONFLICT(nominal) DO NOTHING;
    """)

    cursor.execute("""
        INSERT INTO ATM_balance (nominal, count)
        VALUES(200, 15)
        ON CONFLICT(nominal) DO NOTHING;
    """)

    cursor.execute("""
        INSERT INTO ATM_balance (nominal, count)
        VALUES(500, 15)
        ON CONFLICT(nominal) DO NOTHING;
    """)

    cursor.execute("""
        INSERT INTO ATM_balance (nominal, count)
        VALUES(1000, 15)
        ON CONFLICT(nominal) DO NOTHING;
    """)

    conn.commit()
    conn.close()


def start():
    is_login = input('Do you have an account?\n1 Yes \n2 No :')
    if is_login == '1':
        i = 0
        while i < 3:
            username = input("Please, enter your name: ")
            password = input("Please, enter your password: ")
            if login(username, password):
                print(f"Hello, {username}!")
                if username == 'admin':
                    admin_menu(username)
                else:
                    menu(username)
                return
            else:
                print(f"Incorrect username or password. Remaining attempts: {2 - i}")
                i += 1
    elif is_login == '2':
        create_user()
    else:
        print("Invalid input. Please enter 1 or 2.")
        return
    

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
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()
            user_id = return_user_id(username)
            if user_id is not None:
                cursor.execute('SELECT balance FROM users_balance WHERE user_id = ?', (user_id,))
                balance = cursor.fetchone()

                if balance is not None:
                    return balance[0]
                else:
                    cursor.execute('INSERT INTO users_balance (user_id, balance) VALUES (?, ?)', (user_id, 0))
                    return 0.0
            else:
                print("User not found.")
                return 0.0
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None    


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
    if not is_count_valid(count):
        print("Invalid amount. Please enter a positive number.")
        return 0.0

    count = float(count)

    min_nominal = min(get_nominals())
    if count % min_nominal != 0:
        rounded_count = int(count // min_nominal) * min_nominal
        change = count - rounded_count
        print(f"Depositing {rounded_count} usd. Returning change: {change} USD")
        count = rounded_count
    else:
        change = 0.0

    new_balance = get_balance(username) + count
    update_balance(username, new_balance)
    record_a_transaction(username, 'deposit', count)
    return count
    

    
def get_nominals():
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT nominal FROM ATM_balance')
            data = cursor.fetchall()

            result_list = [nominal for nominal, in data]

            return result_list
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return []


def withdraw(username):
    count = input("How much would you like to withdraw from your balance? ")
    if is_count_valid(count):
        current_balance = get_balance(username)
        if not float(count) > current_balance:
            new_balance = get_balance(username) - float(count)
            update_balance(username, new_balance)
            record_a_transaction(username, 'withdrawing', count)
            return count
        else:
            print("Not enough funds in the account.")
            return 0.0
    else:
        print("Invalid amount. Please enter a positive number.")
        return 0.0


def update_balance(username, new_balance):
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()
            user_id = return_user_id(username)
            if user_id is not None:
                cursor.execute("""
                    UPDATE users_balance SET balance = ? 
                    WHERE user_id = ?
                """, (new_balance, user_id))
                return new_balance
            else:
                print("User not found.")
                return None
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None


def record_a_transaction(username, operation, count):
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()
            user_id = return_user_id(username)
            if user_id is not None:
                cursor.execute("""
                    INSERT INTO users_transactions (user_id, amount, transaction_name) 
                    VALUES(?, ?, ?)""", (user_id, count, operation))
            else:
                print("User not found.")
                return None
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None    
 

def admin_menu(username):
    no_exit = True
    
    while no_exit:
        action = input("Please, enter your action: \n1 (Check your balance) \n2 (Аccount replenishment)\n3 (Withdraw money from the account)\n4 (Exit)\n5 (Check quantity of banknotes in the atm)\n6 (cash handling)")
        if action == '1':
            print(f"Your balance: {get_balance(username)}")
        elif action == '2':
            print(f"Deposit: +{deposit(username)} usd")
        elif action == '3':
            print(f"Withdraw: - {withdraw(username)} usd")
        elif action == '4':
            print("You have successfully logged out.")
            no_exit = False
        elif action == '5':
            print(f"Balance in the atm: {get_quantity_of_banknotes()}")
            print(f"Actual balance : {get_atm_balance()}")
        elif action == '6':
            cash_handling()
        else:
            print('Incorrect operation.Try again')


def get_quantity_of_banknotes():
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT nominal, count FROM ATM_balance')
            data = cursor.fetchall()

            if data is not None:
                result_dict = {nominal: count for nominal, count in data}
                return result_dict
            else:
                print("ATM balance not found.")
                return None
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None


def get_atm_balance():
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT nominal, count FROM ATM_balance')
            data = cursor.fetchall()
            result_list = [nominal * count for nominal, count in data]
            balance = sum(result_list)
            return balance
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None  
    

def return_count_of_banknotes(nominal):
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT count FROM ATM_balance WHERE nominal = ?', (nominal,))
            data = cursor.fetchone()

            if data is not None:
                return data[0]
            else:
                return None
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None   


def update_atm_balance_withdraw(nominal, count):
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()

            current_count = return_count_of_banknotes(nominal)

            if current_count is not None and current_count >= count:
                cursor.execute("""
                    UPDATE ATM_balance SET count = ?
                    WHERE nominal = ?
                """, (current_count - count, nominal))
                print(f"Withdrawal successful: {count} banknotes of {nominal} nominal")
            else:
                print(f"Unable to withdraw {count} banknotes of {nominal} nominal. Insufficient quantity in the ATM.")

    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None
    

def update_atm_balance_deposit(nominal, count):
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()

            current_count = return_count_of_banknotes(nominal)

            cursor.execute("""
                UPDATE ATM_balance SET count = ?
                WHERE nominal = ?
            """, (current_count + count, nominal))
            print(f"Deposit successful: {count} banknotes of {nominal} nominal")
    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None
        

def cash_handling():
    try:
        with sl.connect(DB_DIR) as conn:
            cursor = conn.cursor()

            nominal = int(input('Please enter a nominal: '))
            operation = int(input('Please enter operation\n1 withdrawing\n2 deposit \n: '))

            if operation == 1:
                count = int(input('Please enter the quantity you want to withdraw: '))
                update_atm_balance_withdraw(nominal, count)
            elif operation == 2:
                count = int(input('Please enter the quantity you want to deposit: '))
                update_atm_balance_deposit(nominal, count)
            else:
                print('Incorrect operation')

    except sl.Error as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    create_db()
    start()