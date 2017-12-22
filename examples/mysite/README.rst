The example site uses django.db.backends.sqlite3 and requires minimal configuration. ::
    
    git clone git@github.com:ghjan/oauth2app.git oauth2app
    cd oauth2app/examples/mysite
    git checkout master
    pip install https://github.com/ghjan/oauth2app/tarball/master
    pip install django
    pip install django-uni-form
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

Visit http://127.0.0.1:8000/ on your local machine and follow the instructions.