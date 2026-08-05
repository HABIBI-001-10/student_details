# Student Management System

A Django-based web application for managing student records with create, read, update, and delete (CRUD) operations. The project includes a simple student management interface, form validation, and a small API app for experimentation.

## Overview

This project demonstrates a clean Django structure for a basic student administration workflow. It is intended for learning, prototyping, and demonstrating CRUD patterns in a web application.

## Features

- Add a new student record
- View all students or a single student by email
- Update an existing student record
- Delete a student record
- Validate input on the form layer
- Store data in SQLite by default

## Project Structure

```text
.
├── api/                     # Sample API app
├── config/       # Project settings and URL routing
├── students/      # Main student management app
├── templates/               # HTML templates for the UI
├── static/                  # Static assets
├── requirements.txt         # Python dependencies
└── manage.py                # Django management entry point
```

## Technology Stack

- Python 3.x
- Django 6.0.7
- Django REST Framework 3.17.1
- SQLite

## Prerequisites

Make sure Python is installed on your system before proceeding.

## Installation

1. Clone the repository
2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply database migrations

```bash
python manage.py migrate
```

5. Start the development server

```bash
python manage.py runserver
```

6. Open the application in your browser at:

```text
http://127.0.0.1:8000/student-management/
```

## Application Routes

The main web routes are:

- `/student-management/` - Home page
- `/student-management/add/` - Add a student
- `/student-management/view/` - View all students
- `/student-management/view/email/<email>/` - View a specific student by email
- `/student-management/update/<id>/` - Update a student
- `/student-management/delete/<id>/` - Delete a student

## Data Model

The `Student` model includes:

- `name`
- `email` (unique)
- `date_of_birth`
- `department`
- `enrollment_date`

## Development Workflow

### Running tests

```bash
python manage.py test
```

### Creating migrations

```bash
python manage.py makemigrations
```

### Creating a superuser

```bash
python manage.py createsuperuser
```

## Notes

- The project currently uses SQLite and `DEBUG=True`, which is suitable for development but not for production.
- The API app exists as a starting point for REST endpoints, but it may need additional URL wiring depending on your intended use.

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests
4. Submit a pull request with a clear summary of the change
