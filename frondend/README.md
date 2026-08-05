# Student Management System — Frontend Prototype

This folder contains the frontend prototype for the student management system. It includes Django template pages and static assets for the student add/view/update flows.

## Contents

- `templates/` — Django HTML templates for home, add student, view student, and update student pages
- `static/css/style.css` — styling for the prototype UI
- `static/js/script.js` — client-side interactions and form behavior

## Purpose

The frontend files in this directory are intended as a design and interaction prototype for the Django backend in `../backend/`.

## Integration note

The backend project is configured to load templates from `backend/templates/`, so `frondend/templates/` and `frondend/static/` are not served automatically.

To use the frontend prototype with the Django backend, either:

1. Copy `frondend/templates/` into `backend/templates/` and `frondend/static/` into `backend/static/`, or
2. Add `frondend/templates/` and `frondend/static/` to `TEMPLATES[0]['DIRS']` and `STATICFILES_DIRS` in `backend/config/settings.py`.

## Notes

- This frontend prototype is designed to accompany the student model and API in `backend/`.
- It is not yet a fully integrated or production-ready UI.
