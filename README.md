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


