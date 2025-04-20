# SimpleWebApplication
A Web Application for a Library Loan System using Flask, Jinja, Shelve, and Bootstrap.

## Description
A simple database app for a Library Loan system, allowing you to:

1. Create
2. Read
3. Update
4. Delete

Two kinds of objects:

1. Users
2. Customers

Customers are a subclass of Users, requiring more data fields to create.


## Purpose
This Web App was originally made following a practical lesson on creating a basic Web App for my Application Development module in Year 1.
The original tutorial was buggy however, with issues being:

1. The "View Users/Customers" pages causing a 500 Server Error when accessing it before the database is created
2. The alert pop-ups for creating, updating, and deleting entries had some styling issues. For example,
   - The pop-ups were too close to the navigation bar
   - Closing animations were abrupt
   - The original HTML for the pop-ups were outdated, causing the close button to render incorrectly

Annoyed by these minor inconveniences, I took it upon myself to fix the Web App over my school holidays. And now, it is done! 🥳

## Local Deployment
Open Command Prompt and run the following commands:
1. `python -m venv .venv` (for Windows) / `python3 -m venv .venv` (for macOS)
2. `.venv\scripts\activate` (for Windows) / `source .venv/bin/activate` (for macOS)
3. `pip install -r requirements.txt`
4. `python app.py` (to run the flask app)
