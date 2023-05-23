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

