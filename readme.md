# Python Django Exercise

## Important commands
- python virtual environment:
    - `workon <env name>`
    - `deactivate`
- django commands
    - `python3 manage.py makemigrations` && `python3 manage.py migrate`
    - `python3 manage.py runserver 0:3000`

## MVC pattern
- urls.py
- models.py
- views.py

## Authentication
- Logged in user
    - `{{ user }}`
    - `{{ user.is_authenticated }}`
    - In views:
        - `@login_required` decorator in view funtions
        - `LoginRequiredMixin`
