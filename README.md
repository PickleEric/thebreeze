# To install
Create and activate a virtual environment. Use Python3 as the interpreter. Suggest locating the venv/ directory outside of the code directory.
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Site at

http://127.0.0.1:8000

Create superuser
python manage.py createsuperuser

enter username and password

will be able to use these to log into admin console at

127.0.0.1:8000/admin
