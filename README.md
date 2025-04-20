# SimpleWebApplication
A Web Application for a Library Loan System using Flask, Jinja, Shelve, and Bootstrap.

[//]: # (TODO: Explain what this Web App Does)
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

[//]: # (TODO: Explain why this Web App was made)
## Purpose
This Web App was originally made following a practical lesson on creating a basic Web App for my Application Development module in Year 1.


[//]: # (TODO: Explain how to launch Web App locally)
## Local Deployment
Open Command Prompt and run the following commands:
1. `python -m venv .venv` (for Windows) / `python3 -m venv .venv` (for macOS)
2. `.venv\scripts\activate` (for Windows) / `source .venv/bin/activate` (for macOS)
3. `pip install -r requirements.txt`
4. `python app.py` (to run the flask app)
