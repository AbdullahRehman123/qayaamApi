# Qayaam API

## Overview

Qayaam API is the backend service for a hostel booking platform, built with Django and Django REST Framework. It provides a comprehensive set of RESTful endpoints to manage users (Tenants and Realtors), property listings, bookings, and a dual feedback system for both listings and tenants.

The platform is designed to connect students or individuals (Tenants) with property owners (Realtors), facilitating the process of finding and booking hostel accommodations.

## Core Features
*   **User Management:**
    *   Dual user roles: `Tenant` and `Realtor`.
    *   Token-based authentication and user registration powered by `Djoser`.
    *   Full CRUD capabilities for user profiles.

*   **Property Listings:**
    *   Realtors can create, manage, and delete their property listings.
    *   Detailed listing information, including price, capacity, address, and available facilities (food, laundry, internet).
    *   Support for uploading multiple photos for each listing.
    *   A `is_featured` flag to highlight specific properties.

*   **Booking System:**
    *   Tenants can book available listings.
    *   Bookings must be approved by the corresponding Realtor.
    *   Endpoints to filter bookings by listing, tenant, or realtor.

*   **Feedback & Rating System:**
    *   **Listing Feedback:** Tenants can provide star ratings and written reviews for listings they have stayed at.
    *   **Tenant Feedback:** Realtors can rate and review tenants, building a reputation system.

*   **API Documentation:**
    *   Integrated Swagger UI for comprehensive and interactive API documentation.

## Technology Stack

*   **Backend:** Python, Django, Django REST Framework
*   **Database:** PostgreSQL
*   **Authentication:** DRF Token Authentication, Djoser
*   **Deployment:** Gunicorn, WhiteNoise (configured for services like Heroku)
*   **API Documentation:** drf-yasg (Swagger)

## Getting Started

Follow these instructions to get a local development environment up and running.

### Prerequisites

*   Python 3.10.2
*   PostgreSQL
*   Git

### Installation
1.  **Clone the repository:**
    ```sh
    git clone https://github.com/abdullahrehman123/qayaamapi.git
    cd qayaamapi
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure the database:**
    *   Make sure you have a PostgreSQL server running.
    *   Create a new database (e.g., `qayaamDB`).
    *   Update the `DATABASES` configuration in `qayaamApi/settings.py` with your PostgreSQL credentials:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_db_name',
                'USER': 'your_db_user',
                'PASSWORD': 'your_db_password',
                'HOST': 'localhost'
            }
        }
        ```

5.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## Project Structure

The project is organized into several Django apps, each handling a specific domain:

*   `qayaamApi/`: Contains the main project settings, configuration, and URL routing.
*   `accounts/`: Manages user accounts, profiles, authentication, and user types (Tenant, Realtor).
*   `listings/`: Handles the creation and management of property listings by Realtors.
*   `booking/`: Manages the booking process, including creation, approval, and retrieval of bookings.
*   `listingsFeedback/`: Manages feedback and ratings submitted by Tenants for listings.
*   `tenantsFeedback/`: Manages feedback and ratings submitted by Realtors for Tenants.

## API Documentation

Once the server is running, you can access the interactive Swagger API documentation in your browser at:

**`http://127.0.0.1:8000/swagger/schema`**

This interface provides a complete list of available endpoints, their required parameters, and allows you to test them directly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
