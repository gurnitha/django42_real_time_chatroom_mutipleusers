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


## 8.3 DJANGO TEMPLATES - Include snippets

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/snippets/footer.html
        new file:   templates/snippets/header.html


## 8.4 DJANGO TEMPLATES - Create home view

        renamed:    templates/app/personal/index.html -> app/personal/templates/personal/home.html
        modified:   app/personal/urls.py
        modified:   app/personal/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/base.html
        new file:   templates/snippets/base_css.html
        new file:   templates/snippets/base_js.html
        modified:   templates/snippets/footer.html
        modified:   templates/snippets/header.html

        NOTE:

        1. Re-arranged the codes to meet the source
        2. Home view successfulle created :)


## 8.5 DJANGO TEMPLATES - Added some snippets to header

        modified:   .gitignore
        modified:   config/settings.py
        modified:   templates/base.html
        modified:   templates/snippets/header.html


## 8.6 DJANGO TEMPLATES - Defining home page with large screen

        modified:   README.md
        modified:   app/personal/urls.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/base.html
        modified:   templates/snippets/footer.html
        modified:   templates/snippets/header.html
        new file:   templates/snippets/header_ori.html

        NOTE:

        It works :)


## 8.7 DJANGO TEMPLATES - Defining home page with small screen

        modified:   README.md
        modified:   templates/snippets/header.html

        NOTE:

        It works :)


## 9. USER MANAGEMENT


#### 9.1 USER MANAGEMENT - Create account app inside app folder

        modified:   README.md
        new file:   app/account/__init__.py
        new file:   app/account/admin.py
        new file:   app/account/apps.py
        new file:   app/account/migrations/__init__.py
        new file:   app/account/models.py
        new file:   app/account/tests.py
        new file:   app/account/views.py


#### 9.2 USER MANAGEMENT - Register the account app to settings.py

        modified:   README.md
        modified:   app/account/apps.py
        modified:   config/settings.py

        NOTE:

        Successfully registered account app :)


#### 9.3 USER MANAGEMENT - Creating custom user model named 'Account' based on the AbstractBaseUser

        modified:   app/account/models.py
        modified:   requirements.txt

        NOTE:

        (venv3942) hp@ING:~ pip install pillow
        ...
        Successfully installed pillow-9.5.0

        (venv3942) hp@ING:~ pip freeze > requirements.txt

        <!-- The custom user model called Account -->

        def get_profile_image_filepath(self, filename):

        """Defining image path for each user"""
        return 'profile_images/' + str(self.pk) + '/profile_image.png'

        def get_default_profile_image():
                """Defining default image path in case user has no image"""
                return "images/logo_1080_1080.png"


        # MODEL:Account
        class Account(AbstractBaseUser):
                """Defining user management in the system"""

                """Defining user creaentials"""
                email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
                username                = models.CharField(max_length=30, unique=True)
                date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
                last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
                is_admin                = models.BooleanField(default=False)
                is_active               = models.BooleanField(default=True)
                is_staff                = models.BooleanField(default=False)
                is_superuser    = models.BooleanField(default=False)
                profile_image   = models.ImageField(max_length=255, 
                                                        upload_to=get_profile_image_filepath, 
                                                        null=True, 
                                                        blank=True, 
                                                        default=get_default_profile_image)
                # Hiding the user's email from other users
                hide_email              = models.BooleanField(default=True)

                # Email and Username are required to create account
                # User must use its email to login
                USERNAME_FIELD = 'email' # Refer to email in line 26
                REQUIRED_FIELDS = ['username'] # Refer to username in line 27

                objects = MyAccountManager()
                
                def __str__(self):
                        return self.username

                # Get profile image of the user from the:get_profile_image_filepath
                def get_profile_image_filename(self):
                        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

                # For checking permissions. to keep it simple all admin have ALL permissons
                def has_perm(self, perm, obj=None):
                        return self.is_admin

                # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
                def has_module_perms(self, app_label):
                        return True


#### 9.4 USER MANAGEMENT - Creating custom user manager model named 'MyAccountManager' based on the BaseUserManager


        <!-- The custom user manager model called MyAccountManager -->

        1. Create MyAccountManager

        class MyAccountManager(BaseUserManager):

        def create_user(self, email, username, password=None):
                if not email:
                        raise ValueError('Users must have an email address.')
                if not username:
                        raise ValueError('Users must have a username.')

                user = self.model(
                        email=self.normalize_email(email),
                        username=username,
                )

                user.set_password(password)
                user.save(using=self._db)
                return user

        def create_superuser(self, email, username, password):
                user = self.create_user(
                        email=self.normalize_email(email),
                        password=password,
                        username=username,
                )
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
                user.save(using=self._db)
                return user

        2. Run migrations

        (venv3942) hp@ING:~ python manage.py makemigrations
        Migrations for 'account':
          app\account\migrations\0001_initial.py
            - Create model Account

        (venv3942) hp@ING:~ python manage.py migrate
        Operations to perform:
          Apply all migrations: account, admin, auth, contenttypes, sessions
        Running migrations:
          Applying account.0001_initial... OK

        3. Check the result

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
         public | account_account            | table | django <<-- new table 
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
        (11 rows)


        django42_real_time_chatroom_mutipleusers=# \dt account_account;
                     List of relations
         Schema |      Name       | Type  | Owner
        --------+-----------------+-------+--------
         public | account_account | table | django
        (1 row)


        django42_real_time_chatroom_mutipleusers=# SELECT * FROM account_account;
         id | password | email | username | date_joined | last_login | is_admin | is_active | is_staff | is_superuser | profile_image | hide_email
        ----+----------+-------+----------+-------------+------------+----------+-----------+----------+--------------+---------------+------------
        (0 rows)


        django42_real_time_chatroom_mutipleusers=# SELECT * FROM auth_user;
         id | password | last_login | is_superuser | username | first_name | last_name | email | is_staff | is_active | date_joined
        ----+----------+------------+--------------+----------+------------+-----------+-------+----------+-----------+-------------
          1 |xxx       |            |t             | admin    |            |           | ....
        (0 rows)


        modified:   README.md
        new file:   app/account/migrations/0001_initial.py
        modified:   app/account/models.py

        NOTE:

        account_acout table created successfully :)


#### 9.5 USER MANAGEMENT - Drop and Recreate database


        NOTE:

        1. Login 

        C:\Users\hp>psql postgres postgres
        Password for user postgres: (admin)
        psql (13.0, server 15.1)
        WARNING: psql major version 13, server major version 15.
                 Some psql features might not work.
        WARNING: Console code page (437) differs from Windows code page (1252)
                 8-bit characters might not work correctly. See psql reference
                 page "Notes for Windows users" for details.
        Type "help" for help.

        postgres=# \l

        ...

        django42_real_time_chatroom_mutipleusers

        2. Drop db

        postgres=# DROP DATABASE django42_real_time_chatroom_mutipleusers;
        DROP DATABASE

        3. Re-create the db

        postgres=# CREATE DATABASE django42_real_time_chatroom_mutipleusers;
        CREATE DATABASE
        
        modified:   README.md

        NOTE:

        1. Due to using custom user, we must drop the db in order to use accout_account table 

        2. Successfully drop and re-create db :)


#### 9.6 USER MANAGEMENT - Setting up AUTH_USER_MODELS in settings.py

        modified:   README.md
        modified:   config/settings.py


#### 9.7 USER MANAGEMENT - Activating the admin app and create superuser

        1. Run migrations

        (venv3942) hp@ING:~ python manage.py makemigrations
        Migrations for 'account':
          app\account\migrations\0001_initial.py
            - Create model Account

        (venv3942) hp@ING:~ python manage.py migrate
        Operations to perform:
          Apply all migrations: account, admin, auth, contenttypes, sessions
        Running migrations:
          No migrations to apply.

        2. Create superuser

        (venv3942) hp@ING:~ python manage.py createsuperuser
        Email: inyoman_gurnitha@yahoo.com
        Username: admin
        Password: admin
        Password (again): admin
        ...
        Superuser created successfully.


        NOTE:

        1. Make sure AUTH_USER_MODEL is correctly setup like this:

        # NEW
        AUTH_USER_MODEL = 'account.Account' # this is correct
        AUTH_USER_MODEL = 'app.account.Account' # this is NOT correct
        AUTH_USER_MODEL = 'app.account.models.Account' # this is NOT correct

        2. If AUTH_USER_MODEL is setup correctly, 
           you will still encounter this error:
           ValueError: Dependency on app with no migrations: account

        3. The above error means that you should run migrations the create superuser

        4. Successfully re-create db and superuser :)

        modified:   README.md
        new file:   app/account/migrations/0001_initial.py


#### 9.8 USER MANAGEMENT - Registering Account model to admin.py

        1. Defining the look of the Account table in admin panel

        modified:   app/account/admin.py
        new file:   media/images/logo_1080_1080.png
        new file:   media_cdn/images/logo_1080_1080.png
        modified:   README.md

        NOTE:

        1. Successfully defining the look of the Account table in admin panel

        2. But the email field is still CASE SENSITIVE. Due to it,
           the same user email, like: inyoman_Gurnixxx@yahoo.com could not
           use for login.
        3. User can login if user use the email like this: inyoman_gurnixxx@yahoo.com
