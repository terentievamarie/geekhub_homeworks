"""
3. Банкомат 2.0: переробіть программу з 
функціонального підходу програмування на використання класів. 
Додайте шанс 10% отримати бонус на баланс при створенні нового користувача.
"""
from pathlib import Path
import os
import sqlite3 as sl
import random


class DataBaseATM:
    def __init__(self):
        self.BASE_DIR = Path(__file__).parent
        self.DB_DIR = os.path.join(self.BASE_DIR, 'ATM.db')
    

    def login(self, login, password):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE login = ? AND password = ?', (login, password))
        user_data = cursor.fetchone()

        conn.commit()
        conn.close()

        if user_data is not None:
            return True
        return False
    

    def create_user(self, username, password):
        if random.random() < 0.10:
            bonus = random.randint(1, 100)
            print(f"Congratulations! You've received a bonus: +{bonus} usd")
        else:
            bonus = 0.0

        if ATM.is_valid_user(username, password):
            if not self.is_user_exists(username): 
                with sl.connect(self.DB_DIR) as conn:
                    cursor = conn.cursor()

                    cursor.execute("""
                        INSERT INTO users (login, password, is_admin)
                        VALUES (?, ?, ?)
                    """, (username, password, 0))

                    cursor.execute("""
                        INSERT INTO users_balance (user_id, balance)
                        VALUES ((SELECT user_id FROM users WHERE login = ?), ?)
                    """, (username, bonus))

                print("User created successfully.")
                return True
            else:
                print("User with this login already exists.")
                return False
        else:
            print("User creation failed. Please check the validity of your username and password.")
            return False
        

    def is_user_exists(self, username):
        try:
            with sl.connect(self.DB_DIR) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT user_id FROM users WHERE login = ?', (username,))
                data = cursor.fetchone()
                return data is not None
        except sl.Error as e:
            print(f"An error occurred: {e}")
            return False
                

    def return_user_id(self, username):
        try:
            with sl.connect(self.DB_DIR) as conn:
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


    def create_db(self):
        conn = sl.connect(self.DB_DIR)
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


    def get_balance(self, username):
        try:
            with sl.connect(self.DB_DIR) as conn:
                cursor = conn.cursor()
                user_id = self.return_user_id(username)
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
        

    def get_nominals(self):
        try:
            with sl.connect(self.DB_DIR) as conn:
                cursor = conn.cursor()
                
                cursor.execute('SELECT nominal FROM ATM_balance')
                data = cursor.fetchall()

                result_list = [nominal for nominal, in data]

                return result_list
        except sl.Error as e:
            print(f"An error occurred: {e}")
            return []
        

    def update_balance(self, username, new_balance):
        try:
            with sl.connect(self.DB_DIR) as conn:
                cursor = conn.cursor()
                user_id = self.return_user_id(username)
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
        

    def record_a_transaction(self, username, operation, count):
        try:
            with sl.connect(self.DB_DIR) as conn:
                cursor = conn.cursor()
                user_id = self.return_user_id(username)
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
        

    def get_quantity_of_banknotes(self):
        try:
            with sl.connect(self.DB_DIR) as conn:
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
        

    def get_atm_balance(self):
        try:
            with sl.connect(self.DB_DIR) as conn:
                cursor = conn.cursor()
                
                cursor.execute('SELECT nominal, count FROM ATM_balance')
                data = cursor.fetchall()
                result_list = [nominal * count for nominal, count in data]
                balance = sum(result_list)
                return balance
        except sl.Error as e:
            print(f"An error occurred: {e}")
            return None  


    def return_count_of_banknotes(self, nominal):
        try:
            with sl.connect(self.DB_DIR) as conn:
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
        

    def update_atm_balance_withdraw(self, nominal, count):
        try:
            with sl.connect(self.DB_DIR) as conn:
                cursor = conn.cursor()

                current_count = self.return_count_of_banknotes(nominal)

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
        

    def update_atm_balance_deposit(self, nominal, count):
        try:
            with sl.connect(self.DB_DIR) as conn:
                cursor = conn.cursor()

                current_count = self.return_count_of_banknotes(nominal)

                cursor.execute("""
                    UPDATE ATM_balance SET count = ?
                    WHERE nominal = ?
                """, (current_count + count, nominal))
                print(f"Deposit successful: {count} banknotes of {nominal} nominal")
        except sl.Error as e:
            print(f"An error occurred: {e}")
            return None
    

class ATM:
    def __init__(self):
        self.db = DataBaseATM()


    def start(self):
        is_login = input('Do you have an account?\n1 Yes \n2 No :')
        if is_login == '1':
            i = 0
            while i < 3:
                username = input("Please, enter your name: ")
                password = input("Please, enter your password: ")
                if self.db.login(username, password):
                    print(f"Hello, {username}!")
                    if username == 'admin':
                        self.admin_menu(username)
                    else:
                        self.menu(username)
                    return
                else:
                    print(f"Incorrect username or password. Remaining attempts: {2 - i}")
                    i += 1
        elif is_login == '2':
            username = input("Please, create your login: ")
            password = input("Please, create your password: ")
            if self.db.create_user(username, password):
                self.menu(username)
                return
        else:
            print("Invalid input. Please enter 1 or 2.")
            return
    

    def menu(self,username):
        no_exit = True
        
        while no_exit:
            action = input("Please, enter your action: \n1 (Check balance) \n2 (Аccount replenishment)\n3 (Withdraw money from the account)\n4 (Exit)")
            if action == '1':
                print(f"Your balance: {self.db.get_balance(username)}")
            elif action == '2':
                print(f"Deposit: +{self.deposit(username)} usd")
            elif action == '3':
                print(f"Withdraw: - {self.withdraw(username)} usd")
            elif action == '4':
                print("You have successfully logged out.")
                no_exit = False
            else:
                print('Incorrect operation.Try again')


    @staticmethod
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
    

    @staticmethod
    def is_count_valid(count):
        try:
            count = float(count)
            if count > 0:
                return True
            return False
        except ValueError as e:
            print(e)


    def deposit(self, username):
        count = input("How much do you want to deposit into your account? ")
        if not self.is_count_valid(count):
            print("Invalid amount. Please enter a positive number.")
            return 0.0

        count = float(count)

        min_nominal = min(self.db.get_nominals())
        if count % min_nominal != 0:
            rounded_count = int(count // min_nominal) * min_nominal
            change = count - rounded_count
            print(f"Depositing {rounded_count} usd. Returning change: {change} USD")
            count = rounded_count
        else:
            change = 0.0

        new_balance = self.db.get_balance(username) + count
        self.db.update_balance(username, new_balance)
        self.db.record_a_transaction(username, 'deposit', count)
        return count
    

    def withdraw(self, username):
        count = input("How much would you like to withdraw from your balance? ")
        if self.is_count_valid(count):
            current_balance = self.db.get_balance(username)
            if not float(count) > current_balance:
                new_balance = self.db.get_balance(username) - float(count)
                self.db.update_balance(username, new_balance)
                self.db.record_a_transaction(username, 'withdrawing', count)
                return count
            else:
                print("Not enough funds in the account.")
                return 0.0
        else:
            print("Invalid amount. Please enter a positive number.")
            return 0.0


    def admin_menu(self, username):
        no_exit = True
        
        while no_exit:
            action = input("Please, enter your action: \n1 (Check your balance) \n2 (Аccount replenishment)\n3 (Withdraw money from the account)\n4 (Exit)\n5 (Check quantity of banknotes in the atm)\n6 (cash handling)")
            if action == '1':
                print(f"Your balance: {self.db.get_balance(username)}")
            elif action == '2':
                print(f"Deposit: +{self.deposit(username)} usd")
            elif action == '3':
                print(f"Withdraw: - {self.withdraw(username)} usd")
            elif action == '4':
                print("You have successfully logged out.")
                no_exit = False
            elif action == '5':
                print(f"Balance in the atm: {self.db.get_quantity_of_banknotes()}")
                print(f"Actual balance : {self.db.get_atm_balance()}")
            elif action == '6':
                self.cash_handling()
            else:
                print('Incorrect operation.Try again')


    def cash_handling(self):
        try:
            nominal = int(input('Please enter a nominal: '))
            operation = int(input('Please enter operation\n1 withdrawing\n2 deposit \n: '))

            if operation == 1:
                count = int(input('Please enter the quantity you want to withdraw: '))
                if count >= 0:
                    self.db.update_atm_balance_withdraw(nominal, count)
                else:
                    print('Enter, please, a positive number')
            elif operation == 2:
                count = int(input('Please enter the quantity you want to deposit: '))
                if count >= 0:
                    self.db.update_atm_balance_deposit(nominal, count)
                else:
                    print('Enter, please, a positive number')
            else:
                print('Incorrect operation')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
        except sl.Error as e:
            print(f"An error occurred: {e}")
            return None
        

if __name__ == '__main__':
    database = DataBaseATM()
    database.create_db()
    atm = ATM()
    atm.start()
 