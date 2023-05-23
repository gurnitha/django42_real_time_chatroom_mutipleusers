# django42_real_time_chatroom_mutipleusers
Belajar membuat aplikasi CHATROOM menggunakan Django versi 4.2

[Github repo](https://github.com/gurnitha/django42_real_time_chatroom_mutipleusers)
Source: C:\TUTORIALS\Django\CodingWithMitch - Real-time Chat Messenger 2021-4

Project: F:\_ingafter65\CHATROOM


## [1. GITHUB-Create Github repo](https://github.com/gurnitha/django42_real_time_chatroom_mutipleusers)


## 2. SETUP


#### 2.1 SETUP - Create virtual environment
	
		1. Check versions

        $ python --version
        Python 3.9.5
        $ pip --version
        pip 23.1.2
        $ virtualenv --version
        virtualenv 20.7.2 

        2. Create virtual environment

        $ python -m venv venv3942

        3. Results

        modified:   README.md
        new file:   venv3942/Scripts/Activate.ps1
        new file:   venv3942/Scripts/activate
        new file:   venv3942/Scripts/activate.bat
        new file:   venv3942/Scripts/deactivate.bat
        new file:   venv3942/Scripts/pip.exe
        new file:   venv3942/Scripts/pip3.9.exe
        new file:   venv3942/Scripts/pip3.exe
        new file:   venv3942/Scripts/python.exe
        new file:   venv3942/Scripts/pythonw.exe
        new file:   venv3942/pyvenv.cfg

        modified:   .gitignore
        modified:   README.md


## 3. CREATE DJANGO PROJECT


#### 3.1 CREATE DJANGO PROJECT - Install Django version 4.2

        $ # Install Django version 4.2

        $ source venv3942/Scripts/activate
        (venv3942)
        $ pip install django==4.2
        ...
        Successfully installed asgiref-3.6.0 django-4.2 sqlparse-0.4.4 tzdata-2023.3


#### 3.2 CREATE DJANGO PROJECT - project's name 'config'

        $ # 1. Create Django Project 'config'

        (venv3942)
        $ django-admin startproject config .

        $ # 2. Check the result using tree command

        (venv3942)
        $ tree config/
        config/
        |-- __init__.py
        |-- asgi.py
        |-- settings.py
        |-- urls.py
        |-- wsgi.py

        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        
        NOTE:

        Perintah ini: $ django-admin startproject config .
        menghasilkan django proyek dibuat di dalam root 
        folder 'django42_real_time_chatroom_mutipleusers'

        TESTING:

        $ # 3. Menajalankan proyek

        (venv3942)
        $ python manage.py runserver

        $ # 4. Buka di browser
        
        http://127.0.0.1:8000/

        HASIL:

        View release notes for Django 4.2
        The install worked successfully! Congratulations!
        You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.

        modified:   .gitignore
        modified:   README.md


#### 3.3 CREATE DJANGO PROJECT - Create requirements.txt file

        1. Check the installed library in venv3942

        (venv3942) hp@ING:~ pip list

        Package    Version
        ---------- -------
        asgiref    3.6.0
        Django     4.2
        pip        21.1.1
        setuptools 56.0.0
        sqlparse   0.4.4
        
        2. Create requirements.txt file

        (venv3942) hp@ING:~ pip freeze > requirements.txt

        !!! NOTE:

        venv3942 MUST BE reside inside the root folder

        modified:   README.md
        new file:   requirements.txt


## 4. DATABASE


#### 4.1 DATABASE - Install postgresql

        PASS


#### 4.2 DATABASE - Create postgresql db

        1. Check if PostgreSQL server is running

        1.1 Open Task Manager > Services
        > find postgresql ..

        Note:

        In this case I found PostgreSQL server is running

        2. Open any terminal (in this case Windows CMD)

        Microsoft Windows [Version 10.0.19045.2965]
        (c) Microsoft Corporation. All rights reserved.

        C:\Users\hp>psql postgres postgres
        Password for user postgres:
        psql (13.0, server 15.1)
        WARNING: psql major version 13, server major version 15.
                 Some psql features might not work.
        WARNING: Console code page (437) differs from Windows code page (1252)
                 8-bit characters might not work correctly. See psql reference
                 page "Notes for Windows users" for details.
        Type "help" for help.

        postgres=# 

        3. Show all databases in the postgres db

        postgres=# \l

        4. Create a new db

        postgres=# CREATE DATABASE django42_real_time_chatroom_mutipleusers;
        CREATE DATABASE

        5. Check if django42_real_time_chatroom_mutipleusers has been created

        postgres=# \l

        modified:   README.md


#### 4.3 DATABASE - Create a new user with password and give all privileges


        NOTE: Continueing the above process

        6. Create a new user with password

        postgres=# CREATE USER django WITH PASSWORD 'password';
        CREATE ROLE

        7. List the users in the db

        postgres=# \du
                                   List of roles
         Role name |                         Attributes                         | Member of
        -----------+------------------------------------------------------------+-----------
         core      | Create DB                                                  | {}
         django    |                                                            | {}
         postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
         supercore | Create DB                                                  | {}

        8. Give the new user (django) all the privileges

        postgres=# GRANT ALL PRIVILEGES ON DATABASE django42_real_time_chatroom_mutipleusers to django;
        GRANT

        modified:   README.md


#### 4.4 DATABASE - Login as the new user

        1. Login as the new user (django) of the 'django42_real_time_chatroom_mutipleusers' db

        C:\Users\hp>psql django42_real_time_chatroom_mutipleusers django
        Password for user django:(password)
        psql (13.0, server 15.1)
        WARNING: psql major version 13, server major version 15.
                 Some psql features might not work.
        WARNING: Console code page (437) differs from Windows code page (1252)
                 8-bit characters might not work correctly. See psql reference
                 page "Notes for Windows users" for details.
        Type "help" for help.

        django42_real_time_chatroom_mutipleusers=>

        2. Check if it has any tables 

        django42_real_time_chatroom_mutipleusers=> \dt

        Did not find any relations.
        django42_real_time_chatroom_mutipleusers=>

        NOTE:

        Successfully logged in 

        :)

        modified:   README.md


#### 4.5 DATABASE Configure the db to use it for the project - Install psycopg2

        1. Install psycopg2

        (venv3942) hp@ING:~ pip install psycopg2
        Collecting psycopg2
        ...

        2. Upgrade pip

        (venv3942) hp@ING:~ python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-23.1.2

        3. Add installed library to requirements.txt file

        (venv3942) hp@ING:~ pip freeze > requirements.txt

        modified:   README.md


#### 4.6 DATABASE Configure the db to use it for the project - Update db in settings.py

        1. Update settings.py

        # New db
        DB_NAME = "django42_real_time_chatroom_mutipleusers"
        DB_USER = "django"
        DB_PASSWORD = "password"

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': DB_NAME,
                'USER': DB_USER,
                'PASSWORD': DB_PASSWORD,
                'HOST': 'localhost',
                'PORT': '5432'
            }
        }

        2. Run the server to test it out

        (venv3942) hp@ING:~ python manage.py runserver

        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        May 23, 2023 - 15:56:29
        Django version 4.2, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        modified:   README.md
        modified:   config/settings.py


## 5. DJANGO ADMIN


#### 5.1 DJANGO ADMIN - Activate django admin

        1. Jalankan migrasi

        (venv3942) hp@ING:~ python manage.py makemigrations
        No changes detected

        (venv3942) hp@ING:~ python manage.py migrate

        Unable to create the django_migrations table (permission denied for schema public
        LINE 1: CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMA...
                             ^
        )

        NOTE:

        Could not create tables

        ASSESMENTS:

        1. GRANT ALL PRIVILEGES ON DATABASE still does not allow the new user 'django' create tables

        postgres=# GRANT ALL PRIVILEGES ON DATABASE django42_real_time_chatroom_mutipleusers to django;
        GRANT

        SOLUTION:

        1. Run postgres admin server
        2. Find Login/Group Roles > properties > 
           in new window clik > superuser

        3. Re-run the migrations

        (venv3942) hp@ING:~ python manage.py makemigrations
        No changes detected

        (venv3942) hp@ING:~ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK

        NOTE:

        Successfully created tables

        modified:   README.md


#### 5.2 DJANGO ADMIN - Using dbshell to check the results


        (venv3942) hp@ING:~ python manage.py dbshell
        psql (13.0, server 15.1)
        WARNING: psql major version 13, server major version 15.
                 Some psql features might not work.
        WARNING: Console code page (437) differs from Windows code page (1252)
                 8-bit characters might not work correctly. See psql reference
                 page "Notes for Windows users" for details.
        Type "help" for help.

        django42_real_time_chatroom_mutipleusers=# \dt
                          List of relations
         Schema |            Name            | Type  | Owner
        --------+----------------------------+-------+--------
         public | auth_group                 | table | django
         public | auth_group_permissions     | table | django
         public | auth_permission            | table | django
         public | auth_user                  | table | django
         public | auth_user_groups           | table | django
         public | auth_user_user_permissions | table | django
         public | django_admin_log           | table | django
         public | django_content_type        | table | django
         public | django_migrations          | table | django
         public | django_session             | table | django
        (10 rows)


        django42_real_time_chatroom_mutipleusers=# \dt auth_user
                  List of relations
         Schema |   Name    | Type  | Owner
        --------+-----------+-------+--------
         public | auth_user | table | django
        (1 row)


        django42_real_time_chatroom_mutipleusers=# SELECT * FROM auth_user;
         id | password | last_login | is_superuser | username | first_name | last_name | email | is_staff | is_active | date_joined
        ----+----------+------------+--------------+----------+------------+-----------+-------+----------+-----------+-------------
        (0 rows)

        modified:   README.md


#### 5.3 DJANGO ADMIN - Create superuser and check the result

        1. Create superuser

        (venv3942) hp@ING:~ python manage.py createsuperuser
        Username (leave blank to use 'hp'): admin
        Email address: admin@admin.com
        Password: (admin)
        Password (again): (admin)
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

        2. Check the result

        django42_real_time_chatroom_mutipleusers=# SELECT * FROM auth_user;
         id | password | last_login | is_superuser | username | first_name | last_name | email | is_staff | is_active | date_joined
        ----+----------+------------+--------------+----------+------------+-----------+-------+----------+-----------+-------------
          1 |xxx       |            |t             | admin    |            |           | ....
        (0 rows)

        NOTE:

        Superuser created successfully :)

        modified:   README.md


## 6. REDIS


#### 6.1 REDIS - Install Memurai

        1. Download Memurai

        https://www.memurai.com/get-memurai

        2. Install Memurai

        C:\Program Files\Memurai\

        Port: 6379

        3. After installation

        Open Task Manager > Services > Check for Memurai ...

        DONE :)

        modified:   README.md


#### 6.2 REDIS - Configure Redis on settings.py
        
        1. Setup redis in settings.py

        # REDIS
        CHANNEL_LAYERS = {
            'default': {
                'BACKEND': 'channels_redis.core.RedisChannelLayer',
                'CONFIG': {
                    "hosts": [('127.0.0.1', 6379)],
                },
            }, 
        }

        2. Tesing: run the server

        System check identified no issues (0 silenced).
        May 23, 2023 - 18:05:31
        Django version 4.2, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        modified:   README.md

        NOTE:

        Successfully installed Redis :)


## 7. DJANGO APP


## 7.1 DJANGO APP - Create django app 'app/personal'

        modified:   README.md
        new file:   app/personal/__init__.py
        new file:   app/personal/admin.py
        new file:   app/personal/apps.py
        new file:   app/personal/migrations/__init__.py
        new file:   app/personal/models.py
        new file:   app/personal/tests.py
        new file:   app/personal/views.py

        modified:   README.md


## 7.2 DJANGO APP - Register the app personal to the project (config)

        modified:   README.md
        modified:   app/personal/apps.py
        modified:   config/settings.py


## 8. DJANGO TEMPLATES


## 8.1 DJANGO TEMPLATES - Hellow world with view, urls and templates

        modified:   README.md
        new file:   app/personal/urls.py
        modified:   app/personal/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/app/personal/index.html

        NOTE:

        Successfully displayed Hello World :)


## 8.2 DJANGO TEMPLATES - Create base template & make template inheritance

        modified:   README.md
        modified:   templates/app/personal/index.html
        new file:   templates/base.html