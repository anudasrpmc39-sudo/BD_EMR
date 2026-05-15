# BD_EMR
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
