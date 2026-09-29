from datetime import datetime, timedelta


# -----------------------------
# Data storage
# -----------------------------

books = {}
members = {}
issued_books = {}

next_book_id = 1
next_member_id = 1


# -----------------------------
# Book Management
# -----------------------------

def add_book():
    global next_book_id

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    category = input("Enter category: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    books[next_book_id] = {
        "title": title,
        "author": author,
        "category": category,
        "available": True
    }

    print(f"Book added successfully. Book ID: {next_book_id}")
    next_book_id += 1


def view_books():
    if not books:
        print("No books found.")
        return

    print("\n----------- Book List -----------")

    for book_id, book in books.items():
        status = "Available" if book["available"] else "Issued"

        print(f"ID       : {book_id}")
        print(f"Title    : {book['title']}")
        print(f"Author   : {book['author']}")
        print(f"Category : {book['category']}")
        print(f"Status   : {status}")
        print("--------------------------------")


def search_book():
    keyword = input("Enter title, author, or category to search: ").strip().lower()

    found = False

    for book_id, book in books.items():
        if (
            keyword in book["title"].lower()
            or keyword in book["author"].lower()
            or keyword in book["category"].lower()
        ):
            status = "Available" if book["available"] else "Issued"

            print(f"\nBook ID: {book_id}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print(f"Status: {status}")

            found = True

    if not found:
        print("No matching book was found.")


def delete_book():
    try:
        book_id = int(input("Enter book ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if book_id not in books:
        print("Book not found.")
        return

    if not books[book_id]["available"]:
        print("This book is currently issued and cannot be deleted.")
        return

    del books[book_id]
    print("Book deleted successfully.")


# -----------------------------
# Member Management
# -----------------------------

def add_member():
    global next_member_id

    name = input("Enter member name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name:
        print("Member name cannot be empty.")
        return

    members[next_member_id] = {
        "name": name,
        "phone": phone,
        "email": email
    }

    print(f"Member added successfully. Member ID: {next_member_id}")
    next_member_id += 1


def view_members():
    if not members:
        print("No members registered.")
        return

    print("\n----------- Member List -----------")

    for member_id, member in members.items():
        print(f"Member ID : {member_id}")
        print(f"Name      : {member['name']}")
        print(f"Phone     : {member['phone']}")
        print(f"Email     : {member['email']}")
        print("-----------------------------------")


# -----------------------------
# Issue and Return
# -----------------------------

def issue_book():
    try:
        book_id = int(input("Enter book ID: "))
        member_id = int(input("Enter member ID: "))
    except ValueError:
        print("Please enter valid numeric IDs.")
        return

    if book_id not in books:
        print("Book not found.")
        return

    if member_id not in members:
        print("Member not found.")
        return

    if not books[book_id]["available"]:
        print("This book is already issued.")
        return

    issue_date = datetime.now()
    due_date = issue_date + timedelta(days=14)

    issued_books[book_id] = {
        "member_id": member_id,
        "issue_date": issue_date,
        "due_date": due_date
    }

    books[book_id]["available"] = False

    print("\nBook issued successfully.")
    print("Issue Date:", issue_date.strftime("%d-%m-%Y"))
    print("Due Date  :", due_date.strftime("%d-%m-%Y"))


def return_book():
    try:
        book_id = int(input("Enter book ID to return: "))
    except ValueError:
        print("Please enter a valid book ID.")
        return

    if book_id not in issued_books:
        print("This book is not currently issued.")
        return

    record = issued_books[book_id]
    return_date = datetime.now()

    overdue_days = (return_date.date() - record["due_date"].date()).days

    if overdue_days > 0:
        fine = overdue_days * 5
    else:
        fine = 0

    books[book_id]["available"] = True
    del issued_books[book_id]

    print("\nBook returned successfully.")

    if overdue_days > 0:
        print(f"Overdue by {overdue_days} day(s).")
        print(f"Fine: Rs. {fine}")
    else:
        print("Book returned on time.")
        print("Fine: Rs. 0")


def view_issued_books():
    if not issued_books:
        print("No books are currently issued.")
        return

    print("\n----------- Issued Books -----------")

    for book_id, record in issued_books.items():
        book = books[book_id]
        member = members[record["member_id"]]

        print(f"Book ID     : {book_id}")
        print(f"Book Title  : {book['title']}")
        print(f"Member      : {member['name']}")
        print(
            f"Issue Date  : "
            f"{record['issue_date'].strftime('%d-%m-%Y')}"
        )
        print(
            f"Due Date    : "
            f"{record['due_date'].strftime('%d-%m-%Y')}"
        )
        print("------------------------------------")


# -----------------------------
# Overdue Books
# -----------------------------

def show_overdue_books():
    if not issued_books:
        print("There are no issued books.")
        return

    today = datetime.now().date()
    found = False

    print("\n----------- Overdue Books -----------")

    for book_id, record in issued_books.items():
        due_date = record["due_date"].date()

        if today > due_date:
            overdue_days = (today - due_date).days
            fine = overdue_days * 5

            member = members[record["member_id"]]
            book = books[book_id]

            print(f"Book ID      : {book_id}")
            print(f"Book Title   : {book['title']}")
            print(f"Member       : {member['name']}")
            print(f"Due Date     : {due_date.strftime('%d-%m-%Y')}")
            print(f"Overdue Days : {overdue_days}")
            print(f"Fine         : Rs. {fine}")
            print("------------------------------------")

            found = True

    if not found:
        print("No overdue books.")


# -----------------------------
# Main Menu
# -----------------------------

def main_menu():
    while True:
        print("\n===================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Add Member")
        print("6. View Members")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. View Issued Books")
        print("10. Show Overdue Books")
        print("0. Exit")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            add_member()

        elif choice == "6":
            view_members()

        elif choice == "7":
            issue_book()

        elif choice == "8":
            return_book()

        elif choice == "9":
            view_issued_books()

        elif choice == "10":
            show_overdue_books()

        elif choice == "0":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Program starts here
if __name__ == "__main__":
    main_menu()
