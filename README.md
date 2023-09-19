# Blog App with Django and PostgreSQL

This is a simple blog application developed using Django and PostgreSQL.

## Dockerized Version (Using Docker and Docker Compose)

### Prerequisites

Before you start, make sure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/febbykuniawan/simple-blog-app-test.git 
    cd simple-blog-app-test
    ```

2. **Build and Run the Docker Containers**

    ```bash
    docker-compose up --build
    ```

    Wait for the containers to be built and started.
   
    Once you see the log message:
    blog_app | Watching for file changes with StatReloader`,
    the application is up and running.

    You can now access the application at [http://127.0.0.1:8000] or (http://localhost:8000).

    > Note: The initial build may take some time as it installs dependencies and sets up the environment.

    Keep this terminal open, and any changes you make to the code will automatically reflect in the running application.

    To stop the application and shut down the containers, press `Ctrl + C` in this terminal.

4. **Database Configuration**

    The database is configured in the `docker-compose.yml` file.



## Non-Dockerized Version

### Prerequisites

Before you start, make sure you have the following installed:
- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/download/)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/febbykuniawan/simple-blog-app-test.git
    cd simple-blog-app-test
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Database Configuration**

    - Create a PostgreSQL database.
    - Update the database configuration in `blogproject/settings.py`:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_database_name',
                'USER': 'your_database_user',
                'PASSWORD': 'your_database_password',
                'HOST': 'your_database_host',
                'PORT': 'your_database_port',
            }
        }
        ```

4. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Application**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000` or `http://localhost:8000`.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:
- Fork the repository.
- Create a new branch and make your changes.
- Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
