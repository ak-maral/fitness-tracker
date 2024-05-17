
# Fitness Tracker - Osanka kg
Final project for Software Engineering done by: Akmaral Nurbek kyzy, Cholpon Abdisukhanova , Nuriza Paishan kyzy

Welcome to the Django backend of the Fitness Tracker project. This backend provides RESTful APIs to support various functionalities of the Fitness Tracker application. Below is a brief overview of the project structure and how to get started.

## Project Structure

The project is structured as follows:

- **`admin/`**: Django admin configuration.
- **`users/`**: App for user authentication and profile management.
- **`trainers/`**: App for managing fitness trainers.
- **`workout/`**: App for creating and managing workout routines.
- **`activities/`**: App for recording and tracking fitness activities.
- **`docs/`**: API documentation using Swagger UI.
- **`settings.py`**: Django settings file.
- **`urls.py`**: URL configurations for routing requests to the appropriate app views.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ak-maral/fitness-tracker.git
```

2. Navigate to the project directory:

```bash
cd fitness-tracker
```

3. Install dependencies (assuming you have Django and other requirements already installed):

```bash
pip install -r requirements.txt
```

4. Run migrations to create necessary database tables:

```bash
python manage.py migrate
```

5. (Optional) Create a superuser for accessing the Django admin panel:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open your web browser and navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) to access the Django admin panel and manage users, trainers, workouts, and activities.

## API Documentation

The API documentation is available at [http://localhost:8000/docs/](http://localhost:8000/docs/), powered by Swagger UI. Here, you can explore the available endpoints and interact with the API.
## Design
For a detailed overview of UI requirements, refer to the [Figma](https://www.figma.com/design/n1Tcvuim018CEobp90AQUZ/Fitness-application?node-id=0%3A1&t=YmOsxaCwmuNtTsyw-1).
## Technical Requirements
For a detailed list of technical requirements, refer to the [Technical Requirements Document](https://docs.google.com/document/d/186CrwjGhxILgq0Uh4SNCXqnJ1ICTPSuxV93aOzs7uLQ/edit?usp=sharing).

## Feedback
Here is feedback for project from a teacher [https://docs.google.com/document/d/1BkWzPiYgw3qhbILh4_sgfgHhnAJIKsSVjeIN7Ygqg8c/edit?usp=sharing](https://docs.google.com/document/d/1BkWzPiYgw3qhbILh4_sgfgHhnAJIKsSVjeIN7Ygqg8c/edit?usp=sharing)
## Contributing

Contributions to this project are welcome! Feel free to open issues for bug reports or feature requests, and submit pull requests with enhancements or fixes.

## Acknowledgements

Thanks to the Django community for providing a robust and flexible web framework.
