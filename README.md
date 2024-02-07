# TODO API

## Details

The Gym API Application project aims to streamline gym management and user interaction. With distinct roles for Admin, Coach, Member, and Visitor, the application facilitates account management, progress tracking, and communication. Key features include authentication, profile management, dashboard views, and interactive functionalities such as ratings and complaints. The project's comprehensive scope addresses the needs of users across various gym-related tasks, fostering efficient communication and engagement. Through its user-friendly interface and tailored functionalities, the Gym Mobile Application seeks to enhance the overall gym experience for all stakeholders.

<div align="center">
   <img src="./assets/images/gym_cover_01.jpg">
</div>

## ⚙ Tools and Technologies used

1. **[Python](https://www.python.org/)**: Primary programming language chosen for its simplicity, readability, and vast ecosystem of libraries and frameworks.
2. **[Django](https://www.djangoproject.com/)**: A high-level Python web framework renowned for its scalability, security features, and rapid development capabilities.
3. **[Django Rest Framework (DRF)](https://www.django-rest-framework.org/)**: Built on top of Django, DRF provides powerful tools for building RESTful APIs, simplifying the creation of web services.
4. **[PostgreSQL](https://www.postgresql.org/)**: A robust open-source relational database management system known for its reliability, extensibility, and support for complex queries and transactions.
5. **[JWT (JSON Web Tokens)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)**: A standard for securely transmitting information between parties as JSON objects, commonly used for authentication and authorization in web applications.
6. **[Docker](https://www.docker.com/)**: Containerization platform that simplifies the deployment and management of applications by packaging them into portable containers, ensuring consistency across different environments.
7. **[Docker Compose](https://docs.docker.com/compose/)**: Tool for defining and running multi-container Docker applications, enabling seamless configuration and orchestration of complex application architectures.

## 🛠 Installation and setup

1. Install Docker [here](https://www.docker.com/get-started/)
2. Install Git [here](https://git-scm.com/downloads)
3. Create a working directory:

   ```bash
   mkdir ~/GYM && cd ~/GYM
   ```

4. Clone the repository

   ```bash
   git clone https://github.com/ak4m410x01/TODO_API/ .
   ```

5. Start the application

   ```bash
    docker-compose up -d
   ```

6. Access API: http://127.0.0.1:8000/api/

7. Access DB: 127.0.0.1:5432

8. Don't forget .env file with variables

| Variable            | Value                                                                 |
| ------------------- | --------------------------------------------------------------------- |
| SECRET_KEY          | 'django-insecure-%2dmqnqj9v2e&8yk\*t=#b+2-=i!45+153*@-g0*=&%1od16z^m' |
| DEBUG               | False                                                                 |
| ALLOWED_HOSTS       | 172.0.0.1,\*                                                          |
| DATABASE_ENGINE     | django.db.backends.postgresql                                         |
| DATABASE_HOST       | db                                                                    |
| DATABASE_PORT       | 5432                                                                  |
| DATABASE_NAME       | gym                                                                   |
| DATABASE_USER       | gym                                                                   |
| DATABASE_PASSWORD   | gym                                                                   |
| EMAIL_BACKEND       | django.core.mail.backends.smtp.EmailBackend                           |
| EMAIL_HOST          | smtp.gmail.com                                                        |
| EMAIL_PORT          | 587                                                                   |
| EMAIL_HOST_USER     | youremail@gmail.com                                                   |
| EMAIL_HOST_PASSWORD | yourapppassword                                                       |
| JWT_SECRET_KEY      | ak4m410x01                                                            |
| POSTGRES_DB         | gym                                                                   |
| POSTGRES_USER       | gym                                                                   |
| POSTGRES_PASSWORD   | gym                                                                   |

note:
these variables are for the lab environment only... don't use these in xxx production environments xxx

---

## PIP Packages

    +-------------------------------+---------+---------------------------+
    | Name                          | Version | Use                       |
    | ----------------------------- | ------- | ------------------------- |
    | Python                        | 3.11.7  | Programming Lang          |
    | Django                        | 5.0.1   | Django Framework          |
    | djangorestframework           | 3.14.0  | Restful Framework         |
    | djangorestframework-simplejwt | 5.3.1   | Restful Framework Jwt     |
    | django-filter                 | 23.5    | Restful Framework filters |
    | django-cors-headers           | 4.3.1   | Restful Framework CORS    |
    | psycopg2-binary               | 2.9.9   | PostgreSQL DB lib         |
    | pthon-decouple                | 3.8     | To use .env file          |
    +-------------------------------+---------+---------------------------+
