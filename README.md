# eCommerce REST API using Django Rest Framework

This project is a simple implementation of an eCommerce REST API built using Django Rest Framework and Postgresql.

## Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/rishabdhar12/drf-ecommerce.git
   ```

2. **Create a Virtual Environment** (recommended)

   ```
   virtualenv venv
   source venv/bin/activate (for Unix or MacOS)
   venv\Scripts\activate (for Windows)
   ```

3. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Configuration**

    Generate secret key using the follwing commands and paste the key in .env file

   ```
    python manage.py shell (Launch shell)
    from django.core.management.utils import get_random_secret_key  
    print(get_random_secret_key())
   ```

5. **Database**
    In local.py file
     ```
     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '<your-db-name>',
            'USER': '<your-db-username>',
            'PASSWORD': '<your-db-password>',
            'HOST': '<your-ip-address>',
            'PORT': '5432',
        }
     }
     ```

4. **Run Migrations**

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**

   ```
   python manage.py runserver
   ```

6. **Accessing the API**

   You can access the API endpoints using a tool like Postman or any HTTP client.

## API Endpoints

- **Docs**

  - `GET /api/schema/docs/`:Swagger Docs 

  ---

This README should provide users with a brief overview of your project, how to set it up, and the available endpoints. You can expand on this with more detailed instructions or additional sections based on your project's complexity and requirements.
