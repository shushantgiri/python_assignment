# Library Management System

books = [
    {"title": "Muna Madan", "author": "Laxmi Prasad Devkota", "available": True},
    {"title": "Seto Dharti", "author": "Amar Neupane", "available": True},
    {"title": "Palpasa Cafe", "author": "Narayan Wagle", "available": False},
    {"title": "Karnali Blues", "author": "Buddhisagar", "available": True},
    {"title": "Summer Love", "author": "Subin Bhattarai", "available": True}
]


def show_books():
    print("\nAvailable Books:")

    for book in books:
        if book["available"]:
            print(book["title"], "-", book["author"])


def borrow_book():
    title = input("Enter book title: ")

    for book in books:
        if book["title"].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print("You borrowed", book["title"])
            else:
                print("Book is already borrowed")
            return

    print("Book not found")


def return_book():
    title = input("Enter book title: ")

    for book in books:
        if book["title"].lower() == title.lower():
            if not book["available"]:
                book["available"] = True
                print("You returned", book["title"])
            else:
                print("Book was not borrowed")
            return

    print("Book not found")


while True:
    print("\n--- Library Management System ---")
    print("1. Show Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        borrow_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        print("Thank you. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")