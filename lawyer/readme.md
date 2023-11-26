# Legal Entities Management System

This Django project provides a management system for legal entities, including Lawyers, Cities, States, and Notaries. It allows you to perform CRUD (Create, Read, Update, Delete) operations on these entities through a RESTful API.

## Features

- **Lawyers:**
  - Name
  - Case Type
  - Phone Number
  - Associated Cities
  - Associated States

- **Cities:**
  - City Number
  - City Name
  - Associated States

- **States:**
  - State Number (Primary Key)
  - State Name

- **Notaries:**
  - Name
  - Registration Number
  - Address
  - Associated Cities
  - Associated States

## Project Structure

- **`legal_entities/`**: Django app containing models, serializers, and views.
- **`api/`**: Contains the RESTful API views.
- **`serializers/`**: Serializer classes for each model.
- **`models/`**: Definition of Django models.
- **`migrations/`**: Database migration files.
- **`templates/`**: HTML templates (if applicable).
- **`static/`**: Static files (CSS, JS, images).

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   
2. **Apply database migrations:**
   ```bash
   python manage.py migrate
3. **Run the development server:**
   ```bash
    python manage.py runserver
4. **Access the API at **
    http://localhost:8000/api/

**API Endpoints**
Lawyers:

GET /api/lawyers/: List all lawyers.
POST /api/lawyers/: Create a new lawyer.
Cities:

GET /api/cities/: List all cities.
POST /api/cities/: Create a new city.
States:

GET /api/states/: List all states.
POST /api/states/: Create a new state.
Notaries:

GET /api/notaries/: List all notaries.
POST /api/notaries/: Create a new notary.

**Additional Notes**
Customize the database settings in settings.py according to your configuration.
Ensure the required Django apps and packages are installed.

**License**
This project is licensed under the MIT License.
