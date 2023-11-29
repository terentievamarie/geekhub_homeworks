"""
2. Створіть за допомогою класів та продемонструйте 
свою реалізацію шкільної бібліотеки (включіть фантазію). 
Наприклад вона може містити класи 
Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
"""
from pathlib import Path
import os
import sqlite3 as sl


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}"
    

class Teacher(Person):
    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.subject = subject

    def __str__(self):
        return f"Name: {self.name}" \
                f"Surname: {self.surname}, Teacher of {self.subject}"

    
class Student(Person):
    def __init__(self, name, surname, grade):
        super().__init__(name, surname)
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}" \
                f"Surname: {self.surname}, Student grade: {self.grade}"
  

class Author:
    def __init__(self, author_name, authors_bd):
        self.author_name = author_name
        self.authors_bd = authors_bd

    def __str__(self):
        return f"Author: {self.author_name}, Birthdate: {self.authors_bd}"
   

class Shelf:
    def __init__(self, bookcase_name, shelf_number, left_number):
        self.bookcase_name = bookcase_name
        self.shelf_number = shelf_number
        self.left_number = left_number

    def __str__(self):
        return f"Bookcase name: {self.bookcase_name}, " \
               f"shelf number: {self.shelf_number}, " \
               f"book number at left: {self.left_number}"


class Category:
    def __init__(self, category_name):
        self.category_name = category_name

    def __str__(self):
        return f"Category name is {self.category_name}"


class Book:
    def __init__(self, name, author: Author, shelf: Shelf, category: Category):
        self.name = name
        self.author = author
        self.shelf = shelf
        self.category = category

    def __str__(self):
        return f"{self.name} lays on the {self.shelf} shelf. " \
               f"Author is {self.author}, category: {self.category} "


class LibraryDB:
    def __init__(self):
        self.BASE_DIR = Path(__file__).parent
        self.DB_DIR = os.path.join(self.BASE_DIR, 'Library.db')

    def create_db(self):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                is_librarian INTEGER DEFAULT 0,
                is_teacher INTEGER DEFAULT 0,
                UNIQUE(name, surname) ON CONFLICT IGNORE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                subject TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                author_name TEXT NOT NULL,
                authors_bd TEXT NOT NULL,
                UNIQUE(author_name)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shelves (
                shelf_id INTEGER PRIMARY KEY AUTOINCREMENT,
                bookcase_name TEXT NOT NULL,
                shelf_number INTEGER NOT NULL,
                left_number INTEGER NOT NULL,
                UNIQUE(bookcase_name, shelf_number)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name TEXT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_name TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                shelf_id INTEGER NOT NULL,
                UNIQUE(book_name, author_id),
                FOREIGN KEY (author_id) REFERENCES authors(author_id),
                FOREIGN KEY (category_id) REFERENCES categories(category_id),
                FOREIGN KEY (shelf_id) REFERENCES shelves(shelf_id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_books (
                user_id INTEGER,
                book_id INTEGER,
                PRIMARY KEY (user_id, book_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (book_id) REFERENCES books(book_id)
            );
        """)

        conn.commit()
        conn.close()

    def get_user_id_by_name(self, name, surname):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT user_id FROM users 
            WHERE name = ? AND surname = ?
        """, (name, surname))

        result = cursor.fetchone()

        conn.close()

        return result[0] if result else None
    
    def user_exists(self, name, surname, is_librarian, is_teacher):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT user_id FROM users
            WHERE name = ? AND surname = ?
            AND is_librarian = ? AND is_teacher = ?
        """, (name, surname, is_librarian, is_teacher))

        result = cursor.fetchone()

        conn.close()

        return True if result else False
    
    def get_book_id_by_name(self, name):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT book_id FROM books 
            WHERE book_name = ? 
        """, (name, ))

        user_id = cursor.fetchone()

        conn.close()

        return user_id[0] if user_id else None

    def add_user(self, user):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        if not self.user_exists(user.name, user.surname, 0, 0):
            cursor.execute("""
                INSERT OR IGNORE INTO users 
                (name, surname, is_librarian, is_teacher)
                VALUES (?, ?, ?, ?)""", (user.name, user.surname, 0, 0))
            conn.commit()
            print(f"User {user.name} {user.surname} added to the database.")
        else:
            print(f"User {user.name} {user.surname} already exists in the database.")

        conn.close()

    def add_book(self, book):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        existing_book_id = self.get_book_id_by_name(book.name)

        if existing_book_id is None:
            cursor.execute("""SELECT * FROM authors 
                           WHERE author_name = ?""", (book.author.author_name,))
            existing_author = cursor.fetchone()
        
            if not existing_author:
                cursor.execute("""
                               INSERT OR IGNORE INTO authors (author_name, authors_bd) 
                               VALUES (?, ?)""",
                               (book.author.author_name, book.author.authors_bd))
                conn.commit()

            cursor.execute("""SELECT * FROM shelves 
                           WHERE bookcase_name = ? AND shelf_number = ?""",
                           (book.shelf.bookcase_name, book.shelf.shelf_number))
            existing_shelf = cursor.fetchone()

            if not existing_shelf:
                cursor.execute("""
                    INSERT OR IGNORE INTO shelves (bookcase_name, shelf_number, left_number) 
                    VALUES (?, ?, ?)""", (book.shelf.bookcase_name, book.shelf.shelf_number, book.shelf.left_number))
                conn.commit()

            cursor.execute("""SELECT * FROM categories 
                           WHERE category_name = ?""", (book.category.category_name,))
            existing_category = cursor.fetchone()

            if not existing_category:
                cursor.execute("""INSERT OR IGNORE INTO categories (category_name) 
                               VALUES (?)""", (book.category.category_name,))
                conn.commit()

            try:
                cursor.execute("""
                    INSERT OR IGNORE INTO books (book_name, author, category, shelf)
                    VALUES (?, ?, ?, ?)""",
                    (book.name, book.author.author_name, book.category.category_name, 
                    f"{book.shelf.bookcase_name}-{book.shelf.shelf_number}")
                )
                conn.commit()
                print(f"Book '{book.name}' added to the database.")
            except sl.IntegrityError:
                print(f"Book '{book.name}' already exists in the database.")
        else:
            print(f"Book '{book.name}' already exists in the database.")

        conn.close()

    def borrow_book(self, user_id, book_id):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM user_books
            WHERE user_id = ? AND book_id = ?
        """, (user_id, book_id))

        existing_entry = cursor.fetchone()

        if not existing_entry:
            cursor.execute("""
                INSERT INTO user_books (user_id, book_id)
                VALUES (?, ?)""", (user_id, book_id))
            conn.commit()
            print("Book borrowed successfully.")
        else:
            print("This book is already borrowed by the user.")

        conn.close()

    def is_book_borrowed(self, user_id, book_id):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM user_books 
            WHERE user_id = ? AND book_id = ?
        """, (user_id, book_id))

        result = cursor.fetchone()

        conn.close()

        return True if result else False
    
    def get_borrowed_books(self, user_id):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT b.book_name, b.author, b.category, b.shelf
            FROM user_books ub
            JOIN books b ON ub.book_id = b.book_id
            WHERE ub.user_id = ?
        """, (user_id,))

        borrowed_books = cursor.fetchall()

        conn.close()

        return borrowed_books

    def show_users(self):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM users
        """)
        users = cursor.fetchall()

        for user in users:
            print(f"User ID: {user[0]}, Name: {user[1]}", end=', ')
            print(f"Surname: {user[2]}, Librarian: {user[3]}, Teacher: {user[4]}")

        conn.close()

    def show_books(self):
        conn = sl.connect(self.DB_DIR)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM books
        """)
        books = cursor.fetchall()

        for book in books:
            print(f"Book ID: {book[0]}, Name: {book[1]}", end='')
            print(f"Author: {book[2]}, Category: {book[3]}, Shelf: {book[4]}")

        conn.close()


if __name__ == '__main__':
    library_db = LibraryDB()
    library_db.create_db()

    new_teacher = Teacher("John", "Doe", "Math")
    new_student = Student("Alice", "Smith", 10)
    library_db.add_user(new_teacher)
    library_db.add_user(new_student)

    book_author = Author("J.K. Rowling", "31.07.1965")
    book_shelf = Shelf("Fantasy Section", 1, 10)
    book_category = Category("Fantasy")
    book = Book("Harry Potter and the Sorcerer's Stone", 
                book_author, book_shelf, book_category)
    library_db.add_book(book)

    alice_id = library_db.get_user_id_by_name("Alice", "Smith")
    harry_potter_id = library_db.get_book_id_by_name(
        "Harry Potter and the Sorcerer's Stone"
    )

    library_db.borrow_book(2, 1)
    library_db.borrow_book(alice_id, 1)

    borrowed_books = library_db.get_borrowed_books(alice_id)
    print(f"Borrowed books for user with ID {alice_id}: {borrowed_books}")
    print("----------------------")

    library_db.show_users()
    print("----------------------")
    library_db.show_books()
 