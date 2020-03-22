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

## Permissions
```python
class BookInstance(models.Model):
    ...
    class Meta:
        ...
        permissions = (("can_mark_returned", "Set book as returned"),)  
```
- Current user's permissions
    - `{{ perms.catalog.can_mark_returned }}` True or False
- ```python
    @permission_required('catalog.can_edit')
    def my_view(request):
```