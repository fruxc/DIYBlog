# DIYBlog

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
python -m pip install virtualenv
pyhton -m virtualenv django
cd django
Scripts\activate
git clone https://github.com/fruxc/DIYBlog
pip3 install -r requirements.txt
```

## Migrations and Server Setup

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
