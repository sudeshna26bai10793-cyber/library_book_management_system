# Project Statement: Library Management System

## Problem Statement

Small libraries may need a straightforward way to keep track of books, members, and loans. When this information is managed informally, it can be difficult to check whether a book is available, identify who borrowed it, and follow up on overdue returns. This project provides a simple command-line application for recording and viewing this information and calculating overdue fines.

## Scope of the Project

The project covers basic library operations through an interactive Python terminal menu. A user can add, view, search, and delete books; register and view members; issue and return books; view active loans; and identify overdue books. Loans have a 14-day period, and overdue fines are calculated at Rs. 5 per day.

The current version is intended for basic, single-session use. Records are stored in memory and are lost when the application exits. It does not include a database, persistent storage, a graphical or web interface, user accounts, or network access.

## Target Users

- Librarians or library staff who need to manage a small catalogue and basic loans
- Teachers, students, or project evaluators demonstrating fundamental library workflows
- Developers learning Python functions, dictionaries, console input/output, and date calculations

## High-Level Features

- **Book catalogue:** Add, list, search by title, author, or category, and delete available books
- **Member records:** Register members and view their contact details
- **Book loans:** Issue available books to registered members with issue and due dates
- **Returns:** Return issued books and make them available again
- **Overdue tracking:** List overdue loans and calculate the fine at Rs. 5 per day
- **Input handling:** Validate required names and numeric IDs, and report invalid menu choices