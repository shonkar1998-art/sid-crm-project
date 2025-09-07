# Simple Django CRM

Basic CRM with Django, HTML/CSS/JS.

## Run locally

1. Create and activate virtualenv:
   ```
   python -m venv .venv
   .venv\\Scripts\\activate   (Windows)
   source .venv/bin/activate  (macOS / Linux)
   ```

2. Install:
   ```
   pip install -r requirements.txt
   ```

3. Create migrations & migrate:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create superuser (optional):
   ```
   python manage.py createsuperuser
   ```

5. Run server:
   ```
   python manage.py runserver
   ```

Open http://127.0.0.1:8000
