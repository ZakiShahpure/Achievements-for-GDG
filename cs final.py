import mysql.connector

class LibraryManagementSystem:
    def __init__(self):
        self.connection = self.create_connection()
        self.create_books_table()

    def create_connection(self):
        connection = mysql.connector.connect(
            host="localHost",
            user="root",
            password="root",
            database="library"
        )
        return connection

    def create_books_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                quantity INT NOT NULL
            )
        """)
        self.connection.commit()

    def add_book(self, title, author, quantity):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)
        """, (title, author, quantity))
        self.connection.commit()
        print("Book added successfully!")

    def delete_book(self, book_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            DELETE FROM books WHERE id = %s
        """, (book_id,))
        self.connection.commit()
        print("Book deleted successfully!")

    def update_book(self, book_id, new_title, new_author, new_quantity):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE books SET title = %s, author = %s, quantity = %s WHERE id = %s
        """, (new_title, new_author, new_quantity, book_id))
        self.connection.commit()
        print("Book updated successfully!")

    def view_books(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM books
        """)
        books = cursor.fetchall()

        if not books:
            print("No books found in the library.")
        else:
            print("Books in the library:")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

if __name__ == "__main__":
    library_system = LibraryManagementSystem()

    while True:
        print("\n1. Add Book\n2. Delete Book\n3. Update Book\n4. View Books\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            quantity = int(input("Enter quantity: "))
            library_system.add_book(title, author, quantity)

        elif choice == 2:
            book_id = int(input("Enter the book ID to delete: "))
            library_system.delete_book(book_id)

        elif choice == 3:
            book_id = int(input("Enter the book ID to update: "))
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            new_quantity = int(input("Enter new quantity: "))
            library_system.update_book(book_id, new_title, new_author, new_quantity)

        elif choice == 4:
            library_system.view_books()

        elif choice == 5:
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
