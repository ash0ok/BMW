class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f"- {book}")

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book}" has been added to the library.')

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You have borrowed "{book}".')
        else:
            print(f'Sorry, "{book}" is not available.')

    def return_book(self, book):
        self.books.append(book)
        print(f'Thank you for returning "{book}".')


def main():
    lib = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            lib.display_books()
        elif choice == '2':
            book = input("Enter book name to add: ")
            lib.add_book(book)
        elif choice == '3':
            book = input("Enter book name to borrow: ")
            lib.borrow_book(book)
        elif choice == '4':
            book = input("Enter book name to return: ")
            lib.return_book(book)
        elif choice == '5':
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
