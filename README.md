# Understanding RESTful API

This project is a simple Django application that demonstrates the use of Django REST framework to create a RESTful API for managing blog posts.

## Project Structure
understanding-RESFUL-API/ ├── mysite/ │ ├── api/ │ │ ├── init.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── migrations/ │ │ │ └── init.py │ │ ├── models.py │ │ ├── serializers.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ ├── db-script.sh │ ├── db.sqlite3 │ ├── manage.py │ ├── mysite/ │ │ ├── init.py │ │ ├── asgi.py │ │ ├── settings.py │ │ ├── urls.py │ │ └── wsgi.py │ └── requirements.txt ├── Dockerfile └── README.md
## Requirements

- Python 3.10+
- Django 4.2.6
- Django REST framework
- Environs

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/willin-broad/understanding-RESFUL-API.git
    cd understanding-RESFUL-API/mysite
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## How It Works

This project uses Django and Django REST framework to create a RESTful API for managing blog posts. The main components of the project are:

- **Models**: Define the structure of the data.
- **Serializers**: Convert complex data types to and from JSON.
- **Views**: Handle the logic for the API endpoints.
- **URLs**: Route the API requests to the appropriate views.

### Models

The `BlogPost` model defines the structure of a blog post with the following fields:
- `title` (CharField): The title of the blog post.
- `content` (TextField): The content of the blog post.
- `published_date` (DateTimeField): The date and time when the blog post was published.

### Serializers

The `BlogPostSerializer` converts `BlogPost` instances to and from JSON. It includes the following fields:
- `id`
- `title`
- `content`
- `published_date`

### Views

The views handle the logic for the API endpoints. The main views are:
- `BlogPostListCreate`: Handles listing all blog posts and creating a new blog post.
- `BlogPostRetrieveUpdateDestroy`: Handles retrieving, updating, and deleting a blog post by ID.

### URLs

The URLs route the API requests to the appropriate views. The main endpoints are:
- `GET /blogposts/`: List all blog posts.
- `POST /blogposts/`: Create a new blog post.
- `GET /blogposts/<int:pk>/`: Retrieve a blog post by ID.
- `PUT /blogposts/<int:pk>/`: Update a blog post by ID.
- `DELETE /blogposts/<int:pk>/`: Delete a blog post by ID.

## What It Does

This project provides a simple RESTful API for managing blog posts. It allows you to:
- List all blog posts.
- Create a new blog post.
- Retrieve a blog post by ID.
- Update a blog post by ID.
- Delete a blog post by ID.

## License

This project is licensed under the MIT License.