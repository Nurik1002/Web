

## Requirements
  *	Python 3.7+
  *	pip (Python package manager)

## Installation & Setup
  * Clone or download this repository.
  * Navigate to the project directory in your terminal.


### Copy the commands below, paste into your terminal, and press Enter:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
### Usage
  Install Dependencies:
```
pip install -r requirements.txt
```

  Apply Database Migrations:

```
python manage.py migrate
```


  Start the Development Server:

```
python manage.py runserver
```


Visit http://127.0.0.1:8000/ in your browser to view the application.

### Create a Superuser (Optional)

To access the Django admin panel:

```
python manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin/ to log in.
