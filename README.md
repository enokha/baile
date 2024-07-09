Django Studio Reservation System
This project is a Django-based system that allows users to create accounts, authenticate, add studio details, and make reservations. It utilizes Docker to ensure easy setup and consistency across different environments.

Features
User Management: Create and manage user accounts.
Authentication: Obtain authentication tokens for API access.
Studio Management: Add and manage studio details.
Reservations: Users can make reservations for studios.
Prerequisites
Before you begin, ensure you have Docker and Docker Compose installed on your machine:
Get Docker
Get Docker Compose
Setup and Installation
Clone the Repository

git clone https://your-repository-url.git
cd your-project-directory
Build the Docker Containers

docker-compose build
Run the Containers

docker-compose up
This command will start all the services defined in your docker-compose.yml, including your Django application and any databases.

Using the API
Once the application is running, you can use the following endpoints to interact with the system:

Create a User
Endpoint: POST /users/
Data:
{
  "username": "newuser",
  "password": "newpassword"
}
Obtain a Token
Endpoint: POST /api-token-auth/
Data:
{
  "username": "newuser",
  "password": "newpassword"
}
Add a Studio
Endpoint: POST /studios/
Header: Authorization: Token <Your_Token>
Data:
{
  "name": "New Studio",
  "location": "Some Location"
}
Make a Reservation
Endpoint: POST /reservations/
Header: Authorization: Token <Your_Token>
Data:
{
  "studio": studio_id,
  "date": "2024-07-10",
  "start_time": "12:00",
  "end_time": "14:00"
}
Managing the Application
To manage your application, use the following Docker Compose commands:

Stopping Containers:

docker-compose down
Viewing Logs:

docker-compose logs
Troubleshooting
Container not starting: Check Docker logs for any errors during startup.
Database issues: Ensure the database configuration in docker-compose.yml matches your Django settings.
Further Help
For more information on Docker, visit the Docker documentation. For Django-related queries, refer to the Django documentation.
