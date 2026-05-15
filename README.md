# EMR Starter Project

A small-scale Electronic Medical Record (EMR) system built with FastAPI and SQLAlchemy.

## Features
- Patient registration
- Clinical visits
- Prescriptions
- Laboratory results
- SQLite database
- Interactive API documentation

## Installation

```bash

python -m venv venv
Windows

venv\Scripts\activate
Linux/macOS

source venv/bin/activate

pip install -r requirements.txt
uvicorn app:app --reload
Open in Browser
•	http://127.0.0.1:8000
•	http://127.0.0.1:8000/docs
Default Admin
•	Username: admin
•	Password: admin123

---

# How to Run

```bash
mkdir emr_project
cd emr_project

# Create the folders and files above

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
uvicorn app:app --reload
Then open:
•	http://127.0.0.1:8000
•	http://127.0.0.1:8000/docs
