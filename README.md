# FastAPI Item API

A simple RESTful API for managing items using FastAPI and SQLAlchemy with SQLite as the database.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create, read, update, and delete (CRUD) items.
- Fetch items by ID or name.
- Simple and intuitive API structure.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/urosbmx/CRUD_API.git
2. Navigate to the project directory
    ```bash
   cd CRUD_API
3. Create a virtual environment and activate it (optional but recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```


## Usage
1. Install the required packages
```bash
pip install -r app/requirements.txt
```
2. Run application
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
3. Run with docker
   ```bash
   docker-compose up --build
   ```
Open your browser and navigate to http://localhost:8000/docs

## Database
The application uses an SQLite database named item.db, which will be created automatically when the application is run for the first time.


## Acknowledgments
FastAPI
SQLAlchemy





