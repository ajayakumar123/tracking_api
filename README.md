
## Objective
This project provides a scalable RESTful API that generates unique 
tracking numbers for parcels, ensuring efficiency and concurrency handling. 
The tracking numbers follow a specific regex pattern

## Prerequisites
Python 3.8+
pip 
Git

## Installation and Setup

### 1. Clone the Repository
https://github.com/ajayakumar123/tracking_api
cd tracking-api

### 2. Set Up a Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Apply Database migration
tracking_api> python manage.py makemigrations
tracking_api> python manage.py migrate

### 5.Run server
tracking_api> python manage.py runserver