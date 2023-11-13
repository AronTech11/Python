class Book:
    def __init__(self, title, author, publication_date, price, category):
        # Initialize book attributes
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.price = float(price)
        self.category = category

    def __str__(self):
        # Define how the book should be formatted as a string
        return f"{self.title}, {self.author}, {self.publication_date}, {self.price}, {self.category}"

class Young(Book):
    def __init__(self, title, author, publication_date, price):
        # Initialize attributes specific to young readers' books
        super().__init__(title, author, publication_date, price, "Young")

class Adult(Book):
    def __init__(self, title, author, publication_date, price):
        # Initialize attributes specific to adult books
        super().__init__(title, author, publication_date, price, "Adult")

def write_book_to_file(book, filename):
    # Write book information to the given file
    with open(filename, "a") as file:
        file.write(f"{book}\n")

def read_books_from_file(filename):
    # Read books from the file and return a list of book objects
    books = []
    with open(filename, "r") as file:
        for line in file:
            book_info = line.strip().split(', ')
            title, author, publication_date, price, category = book_info
            if category == "Young":
                book = Young(title, author, int(publication_date), float(price))
            else:
                book = Adult(title, author, int(publication_date), float(price))
            books.append(book)
    return books

# You may add more methods as needed for your implementation.
