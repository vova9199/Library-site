# Library Management System

## Project Description

The Library Management System is a sophisticated software solution designed to efficiently manage a library's resources and operations. This project harnesses the power of Django, a high-level Python web framework, and Docker containerization to deliver a robust and scalable library management system.

### Key Features

- **User Management:** The system allows both librarians and visitors to register and manage their accounts. Librarians enjoy special privileges to oversee the library's operations, while visitors can borrow books.

- **Catalog Management:** Librarians can easily add, edit, or remove books from the library's catalog. Each book entry is equipped with essential details such as title, author, ISBN, and availability status.

- **Borrowing and Returning:** Visitors can browse the library's catalog, check book availability, and borrow titles. The system diligently keeps track of due dates and sends timely reminders.

- **User Authentication:** User data is securely managed with robust authentication and authorization. Passwords are diligently hashed and protected. Visitors can conveniently reset their passwords in case of a lapse in memory.

- **Role-Based Access Control:** Different roles (e.g., librarian, visitor) enjoy various levels of access to the system's features. Librarians wield the power to manage the catalog, while visitors can conveniently borrow and return books.

- **Search and Filter:** The system offers an intuitive search and filter functionality to assist users in locating books quickly. Users can perform searches by title, author, or category.

- **Responsive Design:** The web application boasts a responsive user interface to ensure a seamless user experience across a variety of devices, including desktops, tablets, and smartphones.

## Getting Started

This GitHub repository contains the complete source code and configuration files needed to set up and run the Library Management System. By utilizing Docker, the application can be containerized and deployed consistently across various environments.

The Library Management System project is an ideal choice for educational institutions, public libraries, and private collections seeking a digital solution to streamline their operations and enhance the user experience.

## Setup and Usage

To get started with the Library Management System, follow these steps:

1. **Clone the Repository:**

git clone https://github.com/your-username/library-management.git


2. **Docker Configuration:**
- Ensure you have Docker installed on your system.
- Create a `.env` file in the project root directory with your PostgreSQL database configuration. Example:

  ```
  DB_NAME=your-database-name
  DB_USER=your-database-user
  DB_PASSWORD=your-database-password
  DB_HOST=db
  DB_PORT=5432
  ```

3. **Run Docker Compose:**
- Build and start the Docker containers using Docker Compose:
  ```
  docker-compose up -d
  ```

4. **Apply Migrations:**
- Apply the initial database migrations to set up the database schema:
  ```
  docker-compose exec web python manage.py makemigrations
  docker-compose exec web python manage.py migrate
  ```

5. **Create a Superuser (Admin):**
- You can create an admin superuser to access the admin panel:
  ```
  docker-compose exec web python manage.py createsuperuser
  ```

6. **Access the Application:**
- Open your web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the Library Management System.

7. **Admin Panel:**
- Access the admin panel by logging in with the superuser credentials at [http://localhost:8000/admin](http://localhost:8000/admin).

8. **Management Commands:**
- You can run management commands within the Docker container. For example, to load initial data, you can use:
  ```
  docker-compose exec web python manage.py loaddata initial_data.json
  ```



