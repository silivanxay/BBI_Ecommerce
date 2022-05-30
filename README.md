# BBI_Ecommerce
Bamboo BI Ecommerce

This application enables Django powered websites to have multiple tenants via PostgreSQL schemas. A vital feature for every Software-as-a-Service website.
        
    # Creat a new database
    CREATE DATABASE 'bbi_ecomm'


# Prerequisites
    pip install psycopg2

# Installation 
Assuming you have django installed, the first step is to install django-tenants.
        
    pip install django-tenants

Basic Settings
You’ll have to make the following modifications to your settings.py file.

Your DATABASE_ENGINE setting needs to be changed to

    DATABASES = {
    'default': {
            # Tenant Engine
            'ENGINE': 'django_tenants.postgresql_backend',
            # set database name
            'NAME': 'bbi_ecomm',
            # set your user details
            'USER': 'postgres',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'POST': '5432'
        }
    }
Suppose we have an app name 'tenent' and we want to create a model called Client.
        
    python manage.py startapp tenant

Make migrations and Apply to database

    # create migrations files
    python manage.py makemigrations
    # Apply migrations
    python manage.py migrate_schemas

Setup Initial User, Tenant and Admin
        
    # create first user
    python manage.py createsuperuser
    # Create the Public Schema
    python manage.py create_tenant
    # Create the Administrator
    python manage.py create_tenant_superuser
    python manage.py runserver