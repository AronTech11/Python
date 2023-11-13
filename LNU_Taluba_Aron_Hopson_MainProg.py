# Name : Taluba Aron Hopson
# Student ID : 101747537
# Date : 3rd November 2023

'''The provided Python code represents a Bookstore Management System. It consists of several classes
and a main program that allows users to interact withthe system and manage a bookstore's inventory.

The classes include:

User: It interacts with the user to retrieve their name and store it as an object attribute.

Book: This class represents a book with attributes for title, author, publication date,
price, and category. It also has a method to display book information.

Young and Adult are subclasses of Book, representing specific book categories:
"Young Readers" and "Adult" They inherit attributes from the Book class.

Bookstore: It manages the bookstore's inventory, allowing users to add, delete, view book information,
and view all books. It reads and writes book data to a file.

The main program, executed when the script runs, involves user interactions through a menu-driven interface.
Users can add, delete, or view books, with separate options to exit the program. Input validation is applied
to ensure accurate data entry. The program is designed to maintain a bookstore's inventory in a text file. 
It provides a user-friendly interface for bookstore management, and the code demonstrates 
object-oriented programming principles and file handling in Python.'''


# Import the necessary classes from the LNU_Taluba_Aron_Hopson_class module
from LNU_Taluba_Aron_Hopson_class import Bookstore, Adult, Young, User

# The main program that orchestrates user interactions and calls the above functions
def main():
    # Initialize a User object to greet the user
    user_name = User()
    
    # Print a welcome message
    print(f"Hello, {user_name.name}! Welcome to the Bookstore Management System.")
    print("This program facilitates reading from and writing to the bookstore's inventory file.")

    # Set the filename for the bookstore's inventory file
    filename = "BookShop.txt"
    bookstore = Bookstore(filename)
    
    while True:
        # Display menu options
        print("1 – Add a book")
        print("2 – Delete a book")
        print("3 – View a book")
        print("4 – View the book file")
        print("5 – Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Input book details
            title = input("Enter the book title: ")
            author = input("Enter the author's last name: ")

            while True:
                try:
                    publication_date = int(input("Enter the publication date: "))
                    break
                except ValueError:
                    print("Invalid input for publication date. Please enter a valid numeric value.")

            while True:
                try:
                    price = float(input("Enter the book price: "))
                    break
                except ValueError:
                    print("Invalid input for price. Please enter a valid numeric value.")

            while True:
                category = input("Enter the book category (Young Readers/Adult): ")
                if category == "Young Readers" or category == "Adult":
                    break
                else:
                    print("Invalid category. Please enter 'Young Readers' or 'Adult'.")
                    continue

            # Check the category and create the appropriate book object
            if category == "Young Readers":
                book = Young(title, author, publication_date, price)
            elif category == "Adult":
                book = Adult(title, author, publication_date, price)

            # Add the book to the bookstore
            bookstore.write_bookshop_file(book)
            print("Book added successfully.")

        # Rest of the code remains the same

        elif choice == "2":
            # Delete a book based on the author's last name
            author_name = input("Enter the author's last name to delete a book: ")
            bookstore.delete_book(author_name)

        elif choice == "3":
            # View book information based on the author's last name
            author_name = input("Enter the author's last name to view a book: ")
            book_info = bookstore.read_bookshop_file(author_name)
            if "Book not found" in book_info:
                print(book_info)
            else:
                print(book_info)

        elif choice == "4":
            # View all books in the bookstore's inventory
            book_list = bookstore.read_all_bookshop_file()
            print("List of Books in Inventory:")
            print(book_list)
            input("Press Enter to return to the main menu.")

        elif choice == "5":
            print(f"Goodbye, {user_name.name}!")
            break

if __name__ == "__main__":
    main()
