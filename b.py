from a import Book, Young, Adult, write_book_to_file, read_books_from_file

# Create or open the BookShop.txt file

def main():
    filename = "BookShop.txt"

    while True:
        print("Welcome to the Bookstore Management Program!")
        print("1 – Add a book")
        print("2 – Delete a book")
        print("3 – View a book")
        print("4 – View the book file")
        print("5 – Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Implement the code to add a book
            title = input("Enter the book title: ")
            author = input("Enter the author's last name: ")
            publication_date = input("Enter the publication date: ")
            price = input("Enter the book price: ")
            category = input("Enter the category (Young/Adult): ")

            if category == "Young":
                book = Young(title, author, int(publication_date), float(price))
            else:
                book = Adult(title, author, int(publication_date), float(price))

            write_book_to_file(book, filename)
            print("The book has been added to the inventory.")
            
        elif choice == "2":
            # Implement the code to delete a book
            author_to_delete = input("Enter the author's last name to delete: ")

            books = read_books_from_file(filename)

            with open(filename, "w") as file:
                for book in books:
                    if book.author != author_to_delete:
                        file.write(f"{book}\n")

            print(f"Books by {author_to_delete} have been deleted from the inventory.")
            
        elif choice == "3":
            # Implement the code to view a book
            author_to_view = input("Enter the author's last name to view: ")

            books = read_books_from_file(filename)

            for book in books:
                if book.author == author_to_view:
                    print("Title, Author, Publication Date, Price, Category")
                    print(book)
                    break
            else:
                print(f"No books by {author_to_view} found in the inventory.")

        elif choice == "4":
            # Implement the code to view the book file
            print("Title, Author, Publication Date, Price, Category")
            books = read_books_from_file(filename)
            for book in books:
                print(book)

        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
