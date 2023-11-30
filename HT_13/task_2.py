# """
# 2. Створіть за допомогою класів та продемонструйте 
# свою реалізацію шкільної бібліотеки (включіть фантазію). 
# Наприклад вона може містити класи 
# Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
# """
# from pathlib import Path
# import os
# import sqlite3 as sl

from pathlib import Path
import os
import sqlite3 as sl
from datetime import datetime

BASE_DIR = Path(__file__).parent
DB_DIR = os.path.join(BASE_DIR, 'library.db')


class Librarian:
    def __init__(self, db):
        self.conn = sl.connect(db)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        """
        Creates the necessary tables in the database if they do not exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                student_first_name TEXT NOT NULL,
                student_last_name TEXT NOT NULL,
                student_grade TEXT NOT NULL,
                school_student_id INTEGER UNIQUE NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                book_name TEXT NOT NULL,
                book_author TEXT NOT NULL,
                is_book_taken TEXT NOT NULL,
                shelf INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES book_categories (category_id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrowed_books (
                return_id INTEGER PRIMARY KEY,
                return_date TEXT NOT NULL,
                student_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (book_id) REFERENCES books (book_id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS book_categories (
                category_id INTEGER PRIMARY KEY,
                category_name TEXT NOT NULL
            )
        """)

        self.conn.commit()

    def student_registration(self, first_name, last_name, student_grade, school_student_id):
        """
        Registers a new student in the system.
        """
        self.cursor.execute("INSERT INTO students (student_first_name, student_last_name, student_grade, "
                            "school_student_id) VALUES (?, ?, ?, ?)",
                            (first_name, last_name, student_grade, school_student_id))
        
        self.conn.commit()

        print(f'{first_name} {last_name} is successfully registered.')

    def is_student_exists(self, school_student_id):
        try:
            self.cursor.execute("""
                        SELECT school_student_id
                        FROM students
                        WHERE school_student_id = ?
                    """, (school_student_id,))
            data = self.cursor.fetchone()
            return data is not None
        except sl.Error as e:
            print(f"An error occurred: {e}")
            return False

    def delete_student(self, student_id):
        self.cursor.execute("SELECT student_first_name FROM students WHERE student_id = ?", (student_id,))
        student_first_name = self.cursor.fetchone()
        self.cursor.execute("SELECT student_last_name FROM students WHERE student_id = ?", (student_id,))
        student_last_name = self.cursor.fetchone()
        if student_first_name and student_first_name[0]:
            self.cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
            self.conn.commit()
            print(f"Student: {student_first_name[0]} {student_last_name[0]} deleted")
        else:
            print(f"Error: Library doesn't have this student yet")

    def add_book(self, book_name, book_author, is_book_taken, shelf, category_id):
        self.cursor.execute("""
                            INSERT INTO books (book_name, book_author, is_book_taken, shelf, category_id)
                            VALUES (?, ?, ?, ?, ?)""",
                            (book_name, book_author, is_book_taken, shelf, category_id))
        
        self.conn.commit()
        print(f"{book_name} added to the library")

    def delete_book(self, book_id):
        self.cursor.execute("""
            DELETE FROM books
            WHERE book_id = ?
        """, (book_id,))
        self.conn.commit()
        print(f"Book with ID {book_id} deleted from the library")

    def return_book_information(self, book_id):
        self.cursor.execute("""SELECT * FROM books
                            WHERE book_id = ?""", (book_id,))
        data = self.cursor.fetchall()
        return data
                    
    def borrow_book(self, student_id, book_id):
        self.cursor.execute("""SELECT is_book_taken FROM books
                    WHERE book_id = ?""", (book_id,))
        is_available = self.cursor.fetchone()
        
        if is_available and is_available[0] == 'available':
            self.cursor.execute("""UPDATE books SET is_book_taken = 'borrowed'
                                WHERE book_id = ?""", (book_id,))
            self.cursor.execute("""INSERT INTO borrowed_books (return_date, student_id, book_id)
                                VALUES (?, ?, ?)""", (datetime.now(), student_id, book_id))
            self.conn.commit()

            print(f"{self.return_book_information(book_id)} borrowed")
        else:
            print('this student cannot borrow this book')

    def pass_the_book(self, student_id, book_id):
        self.cursor.execute("SELECT is_book_taken FROM books WHERE book_id = ?", (book_id,))
        is_available = self.cursor.fetchone()
        if is_available and is_available[0] == 'borrowed':
            self.cursor.execute("""UPDATE books SET is_book_taken = 'available' 
                                WHERE book_id = ?""", (book_id,))
            self.cursor.execute("INSERT INTO borrowed_books (return_date, student_id, book_id) VALUES (?, ?, ?)",
                                (datetime.now(), student_id, book_id))
            
            self.conn.commit()
            print(f"{self.return_book_information(book_id)} passed.")
        else:
            print("The book was not borrowed")

    def show_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        all_books = self.cursor.fetchall()

        if all_books:
            print("\nList of all books in the library:")
            for book in all_books:
                print(f"Book ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Status: {book[3]}, Shelf: {book[4]}, Category ID: {book[5]}")
        else:
            print("The library is currently empty.")

    def show_students(self):
        self.cursor.execute("SELECT * FROM students")
        students = self.cursor.fetchall()

        if students:
            print("List of students:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]} {student[2]}, Grade: {student[3]}, Student ID: {student[4]}")
        else:
            print("No students found in the library.")
        
    def menu(self):
        no_exit = True

        while no_exit:
            action = input("Please, enter your action: \n1 add book \n2 delete book \n3 borrow the book \n4 pass the book \n5 register the student \n6 show books \n7 show students \n8 exit \n:")
            if action == '1':
                book_name = input("Please, enter book's name:")
                book_author = input("Please, enter book's author:")
                is_book_taken = input('enter available/borrowed: ')
                shelf = input("Please, enter shelf: ")
                category_id = input("Enter a category ID: ")
                self.add_book(book_name, book_author, is_book_taken, shelf, category_id)
            elif action == '2':
                book_id = input('Please, enter book_id: ')
                self.delete_book(book_id)
            elif action == '3':
                student_id = int(input('Enter student ID:'))
                book_id = input('Please, enter book_id: ')
                self.borrow_book(student_id, book_id)
            elif action == '4':
                student_id = int(input('Enter student ID:'))
                if self.is_student_exists(student_id):
                    book_id = input('Please, enter book_id: ')
                    self.pass_the_book(student_id, book_id)
                else:
                    print("No this student in the database")
            elif action == '5':
                first_name = input("Enter students name: ")
                last_name = input("Enter the student's last name: ")
                student_grade = input("Enter student grade: ")
                school_student_id = input("Enter student ID: ")
                self.student_registration(first_name, last_name, student_grade, school_student_id)
            elif action == '6':
                self.show_all_books()
            elif action == '7':
                self.show_students()
            elif action == '8':
                print("You left the library")
                no_exit = False


if __name__ == '__main__':
    librarian = Librarian(DB_DIR)
    librarian.create_tables()
    librarian.menu()
 