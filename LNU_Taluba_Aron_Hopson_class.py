class User:
    def __init__(self):
        # Initialize User object and retrieve user's name
        self.name = self.greet_user()
    
    # Greets the user and retrieves their name
    def greet_user(self):
        while True:
            user_name = input("Please enter your name: ")
            if user_name.strip():
                return user_name

class Book:
    def __init__(self, title, author, publication_date, price, category):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author's name.
            publication_date (str): The publication date of the book.
            price (float or str): The price of the book (as float or string).
            category (str): The category of the book.

        Attributes:
            title (str): The title of the book.
            author (str): The author's name.
            publication_date (str): The publication date of the book.
            price (float): The price of the book (as a float).
            category (str): The category of the book.
        """
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.price = float(price)
        self.category = category

    def display(self):
        """
        Returns a formatted string representing the book's details.

        Returns:
            str: Formatted book information.
        """
        return f"{self.title}, {self.author}, {self.publication_date}, ${self.price:.2f}, {self.category}"

class Young(Book):
    def __init__(self, title, author, publication_date, price):
        """
        Initializes a Young Readers book.

        Args:
            title (str): The title of the book.
            author (str): The author's name.
            publication_date (str): The publication date of the book.
            price (float or str): The price of the book (as float or string).

        Attributes:
            Inherits attributes from the Book class and sets the category to "Young Readers".
        """
        # Call the parent class constructor (Book) to initialize the Young object with specific attributes.
        super().__init__(title, author, publication_date, price, "Young Readers")

class Adult(Book):
    def __init__(self, title, author, publication_date, price):
        """
        Initializes an Adult book.

        Args:
            title (str): The title of the book.
            author (str): The author's name.
            publication_date (str): The publication date of the book.
            price (float or str): The price of the book (as float or string).

        Attributes:
            Inherits attributes from the Book class and sets the category to "Adult".
        """
        # Call the parent class constructor (Book) to initialize the Adult object with specific attributes.
        super().__init__(title, author, publication_date, price, "Adult")

class Bookstore:
    """
    Initializes a Bookstore.

    Args:
        filename (str): The filename for the bookstore's inventory file.

    Attributes:
        filename (str): The filename for the inventory file.
    """
    def __init__(self, filename):
        self.filename = filename

    def write_bookshop_file(self, book):
        """
        Adds a book to the bookstore's inventory.

        Args:
            book (Book): The book to be added.
        """
        with open(self.filename, "a") as file:  # Open the inventory file for appending
            # Write the book's formatted information to the file followed by a newline character.
            file.write(f"{book.display()}\n")

    def delete_book(self, author_name):
        """
        Deletes a book from the inventory by the author's name.

        Args:
            author_name (str): The author's name to identify the book to be deleted.
         """
        if not author_name.strip():  # Check if the author's name is empty
            print("Author's name cannot be empty.")
            return

        temp_filename = "temp_BookShop.txt"  # Create a temporary file
        found = False  # Initialize a flag to check if books by the author were found
        with open(self.filename, "r") as original, open(temp_filename, "w") as temp:  # Open temporary file for writing
            for line in original:
                if author_name not in line:
                    temp.write(line)
                else:
                    found = True  # Set the flag to True if a book by the author is found
        import os
        os.remove(self.filename)  # Remove the original file
        os.rename(temp_filename, self.filename)  # Rename the temporary file back to the original filename

        if found:
            print(f"Book by {author_name} deleted successfully.")
        else:
            print(f"No books by {author_name} found in the inventory.")
    
    def read_bookshop_file(self, author_name):
        """
        Views book information by the author's name.

        Args:
            author_name (str): The author's name to search for.

        Returns:
            str: The book information if found; "Book not found." if not found.
        """
        with open(self.filename, "r") as file:  # Open the inventory file for reading
            for line in file:
                book_info = line.strip().split(", ")
                if len(book_info) >= 5 and author_name in book_info[1]:
                    # Convert the price string to a float after removing the dollar sign '$'.
                    price = float(book_info[3].replace('$', ''))
                    # Format the book information with appropriate labels and placeholders for display.
                    return f"Title: {book_info[0]}\nAuthor: {book_info[1]}\nPublication Date: {book_info[2]}\nPrice: ${price:.2f}\nCategory: {book_info[4]}\n"

        return "Book not found."

    def read_all_bookshop_file(self):
        """
        Views all books in the inventory.

        Returns:
            str: A string containing the list of all books.
        """
        with open(self.filename, "r") as file:  # Open the inventory file for reading
            book_list = file.readlines()

        if not book_list:
            return "No books in the inventory."

        return "\n".join(book_list)