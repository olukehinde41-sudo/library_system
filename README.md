NAME: OLUWADARE KEHINDE EMMANUEL
MATRIC:24/14016
DEPARTMENT: COMPUTER SCIENCE

Project: Simple Library Management System

SDLC Phases1. Planning- Project Goal: Develop a simple library management system to manage books, members, and borrowing records.
- Scope:
    - Manage books (add, edit, delete, search)
    - Manage members (add, edit, delete, search)
    - Manage borrowing records (borrow, return)

2. Analysis- Requirements:
    - Book management (ISBN, title, author, quantity)
    - Member management (ID, name, email)
    - Borrowing management (borrow date, return date)
- Use Cases:
    - Add book
    - Borrow book
    - Return book

3. Design- Database Design:
    - Books (ISBN, title, author, quantity)
    - Members (ID, name, email)
    - Borrowings (ID, ISBN, member_ID, borrow_date, return_date)
- Class Diagram:
    - Book
    - Member
    - Borrowing

4. Implementation
5. Testing- Test adding books
- Test borrowing books
- Test returning books

6. Deployment- Deploy as a simple Python app or web app