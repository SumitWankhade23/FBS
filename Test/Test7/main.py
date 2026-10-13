from book import StoreBook
books = {}          
def add_book():
    try:
        bid = int(input("Enter book id: "))
        if bid in books:
            print("A book with this id already exists.")
            return
        name = input("Enter book name: ")
        price = float(input("Enter price: "))
        author = input("Enter author: ")
    except ValueError:
        print("Invalid input Id.")
        return
    books[bid] = StoreBook(bid, name, price, author)
    print("Book added successfully")

def delete_book():
    try:
        bid = int(input("Enter book id to delete: "))
    except ValueError:
        print("Invalid id.")
        return
    if bid in books:
        removed = books.pop(bid)
        print(f"Deleted: {removed.name}")
    else:
        print("Book not found")

def display_all():
    if not books:
        print("No books available")
        return
    for book in books.values():
        book.display()


def search_book():
    try:
        bid = int(input("Enter book id to search: "))
    except ValueError:
        print("Invalid id")
        return
    book = books.get(bid)
    if book:
        print("Book found:")
        book.display()
    else:
        print("Book not found.")


def main():
    while True:
        print("1. Add Book")
        print("2. Delete Book by id")
        print("3. Display all Books")
        print("4. Search Book by id")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            display_all()
        elif choice == "4":
            search_book()
        elif choice == "5":
            print("Than you")
            break
        else:
            print("Invalid choice..")


if __name__ == "__main__":
    main()
