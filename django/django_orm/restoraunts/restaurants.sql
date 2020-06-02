CREATE DATABASE practice_db;

CREATE  TABLE RESTAURANT
(
id INT,
name VARCHAR(255)
);

CREATE  TABLE STAFF
(
id INT,
name VARCHAR(255),
position VARCHAR(255)
);

CREATE  TABLE COUNTRIES
(
id INT,
name VARCHAR(255)
);

CREATE  TABLE CITIES
(
id INT,
name VARCHAR(255)
);

CREATE  TABLE DISHES
(
id INT,
name VARCHAR(255),
calorific VARCHAR(255),
price VARCHAR(255)
);

CREATE  TABLE MENU
(
id INT,
name VARCHAR(255),
season VARCHAR(255)
);

CREATE INDEX name ON cities(name);

ALTER TABLE dishes
ALTER name SET DEFAULT 'NULL';

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'practice_db',
        'USER': 'cursor',
        'PASSWORD': 'very_secret_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}








