<!-- virtual environment install -->
pip install virtualenv

<!-- create virtual environment -->
python -m venv env
<!-- or -->
virtualenv env

<!-- activate virtual environment -->
env\Scripts\activate  (cmd, ps)
env/Scripts/activate
source env\Scripts\activate

<!-- install django -->
pip install Django

<!-- create new project -->
django-admin startproject projectname .  <!-- fullstop is optional -->

<!-- run server/project -->
python manage.py runserver
py manage.py runserver

<!-- create app -->
python manage.py startapp Todolist  <!--Todolist is the name of the app -->

<!-- freeze the installed packages -->
pip freeze > requirements.txt

<!-- un/install requirements.txt -->
pip install -r requirements.txt
pip uninstall -r requirements.txt