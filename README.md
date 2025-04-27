# Airport API Service ✈️🌎📆

**Welcome to the global airport flight tracking system:**
* The Airport API Service, built with Django, efficiently manages and tracks flights from worldwide airports.
* This system facilitates effective coordination and information management.
* The system's structured features allow users to manage various aspects of the aviation ecosystem.

🏞 Airport API Endpoints:

Airport API endpoints

**Project Features:**
* Authentication: Users are authenticated with JWTs issued at login for secure access.
* Admin Panel: Admins can manage data efficiently by adding, editing, and deleting entries.
* Documentation: API documentation is available via Swagger UI.
* Airplane Management: Define and categorize different types of airplanes, capturing details like capacity.
* Crew Management: Manage crew members, including their first and last names.
* Location Handling: Record country and city information, linking airports to nearby big cities.
* Airport Details: Store detailed airport data, including names, cities, and images.
* Route Definition: Define routes between airports to organize flight connections.
* Flight Tracking: Monitor flights with route, airplane, departure, arrival times, and crew details.
* Order and Ticket System: Manage user orders and tickets with flight, row, and seat details.

🏞 Swagger Documentation:

Swagger documentation

**Installation and Usage:**
* Install Python 3.9.
* Install PostgreSQL and create db.
* Install Docker.
* Clone the repository.
* Set up environment variables using ".env.sample" as a guide.
* Run the application.
* Feel free to explore and contribute!

```
git clone https://github.com/frank0190/airport-api-service

(for Windows)
python -m venv venv
source venv/Scripts/activate

(for Mac/Linux)
python3 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

set DJANGO_SECRET_KEY=<your secret key>
set DJANGO_DEBUG=<your debug value>
set DJANGO_ALLOWED_HOSTS=<your allowed hosts>
set POSTGRES_HOST=<your Postgres host>
set POSTGRES_DB=<your Postgres database>
set POSTGRES_USER=<your Postgres user>
set POSTGRES_PASSWORD=<your Postgres password>

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Run with Docker:
docker-compose build
docker-compose up

🏞 DB Structure:

DB structure

**Stages of Project Creation:**
* Initialization of the Project:
  - Set up the initial Django project structure.
  - Configure project settings such as database connection and Django applications.
* Environment Setup:
  - Add the requirements.txt file and environment variables (SECRET_KEY, PostgreSQL settings) in ".env.sample".
  - Switch to the PostgreSQL database and change TIME_ZONE.
* App Structure Organization:
  - Create empty User and Airport apps.
  - Add these apps to INSTALLED_APPS.
* Model Creation:
  - Implement User and UserManager models without the username field.
  - Create Country, City, Airport, Route, Flight, Order, Ticket, AirplaneType, Airplane and Crew models.
  - Add verbose names and unique constraints.
* Migrations and Admin Setup:
  - Create initial migrations and register models in the admin site.
  - Implement UserAdmin without the username field.
* Authentication and Authorization Setup:
  - Add REST framework and JWTAuthentication.
  - Configure permission and throttle classes.
  - Add settings for drf_spectacular.
* ViewSets and Serializers Creation:
  - Implement ViewSets and serializers for AirplaneType, Airplane, Airport, Route, Flight, Order and Ticket.
  - Add filters and configurations for serializers.
* Testing:
  - Implement tests for admin and unauthenticated requests.
  - Create tests for CRUD operations and data filtering.
* Docker:
  - Create Dockerfile, .dockerignore and docker-compose.yml.
* Documentation:
  - Update README.md with the project description.
  - Add images and other materials in the images directory.
  - Update database structure and project description.
* Additional Changes and Fixes:
  - Fix and improve save methods in models.
  - Update .gitignore to include new directories.
  - Refactor code using "black" and "flake8".

🏞 Admin Page:

Admin page

**Getting Access:**

create a user via: /api/user/register
get access token via: /api/user/token
