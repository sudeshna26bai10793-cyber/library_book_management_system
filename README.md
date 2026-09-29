# Library Management System

## Overview

A command-line library management application written in Python. It lets a user maintain a temporary catalogue of books and members, manage book loans, and check overdue returns and fines.

## Features

- Add, view, search, and delete books
- Register and view library members
- Issue books to members and return them
- View currently issued books and their due dates
- Find overdue books and calculate fines at Rs. 5 per overdue day
- Set a 14-day loan period for each issued book

## Technologies and Tools

- Python 3
- Python standard library: `datetime` and `timedelta`
- Any code editor or terminal that can run Python

## Installation and Run

1. Install Python 3 if it is not already installed. Verify it from a terminal:

   ```powershell
   python --version
   ```

2. Open a terminal in the project folder, the folder containing `vityarthi project.py`.

3. Start the application:

   ```powershell
   python "vityarthi project.py"
   ```

4. Choose an option from the menu and follow the prompts. Choose `0` to exit.

No third-party packages are required. Book, member, and loan data is kept in memory and is cleared when the program exits.

## Testing

There is no automated test suite included. Test the application manually:

1. Add a book and a member, then view each list to confirm they appear.
2. Search for the book using part of its title, author, or category.
3. Issue the book using its book ID and the member ID; confirm the due date is 14 days after the issue date.
4. View issued books and confirm the loan is listed and the book is marked issued.
5. Try issuing the same book again and confirm the application rejects it.
6. Return the book and confirm it becomes available again. The fine is Rs. 5 per day if returned after its due date.
7. Try invalid menu choices and non-numeric IDs to confirm the application handles them without stopping.



