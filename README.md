# Student Management System

A Django-backed student record management prototype with a REST API and a separate frontend template prototype.

## Repository overview

This repository is organized into two main pieces:

- `backend/` — Django project and `students` app with data model, REST endpoint, and management tooling.
- `frondend/` — frontend template prototype consisting of Django HTML templates, CSS, and JavaScript.

> Note: The frontend prototype in `frondend/` is not wired into the backend automatically. To serve the UI from the Django project, move or link `frondend/templates/` into `backend/templates/` and `frondend/static/` into `backend/static/`, or update `backend/config/settings.py` to include those paths.

## Key features

- Student data model with:
  - `name`
  - `email` (unique)
  - `date_of_birth`
  - `department`
  - `enrollment_date` (auto-populated)
- Django REST Framework API endpoint for listing student records
- SQLite database for local development
- A frontend prototype for add/view/update student workflows

## Technology stack

- Python 3.11+
- Django 6.0.7
- Django REST Framework 3.17.1
- SQLite

## Getting started

### Prerequisites

- Python 3.11 or later
- Git (optional)

### Installation

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

### Running the development server

```powershell
python manage.py runserver
```

Open the application in your browser at:

```text
http://127.0.0.1:8000/
```

## Available endpoints

- `GET /students/api/students/` — list all student records as JSON
- `GET /admin/` — Django admin interface

## Development workflow

### Run tests

```powershell
python manage.py test
```

### Create migrations

```powershell
python manage.py makemigrations
```

### Create a superuser

```powershell
python manage.py createsuperuser
```

## Notes

- `DEBUG` is enabled by default in `backend/config/settings.py`; this is appropriate for development only.
- A static `SECRET_KEY` is stored in the backend settings file for convenience; replace it before deploying.
- The current implementation includes a REST API endpoint and a student model. The frontend templates in `frondend/` are a separate prototype and may require integration.

## Contributing

1. Create a feature branch.
2. Implement your change.
3. Run tests locally.
4. Open a pull request with a clear summary and relevant details.
