# Flask User CRUD API

based  that uses MongoDB for data storage. The application is Dockerized.

## Requirements

- Docker
- Docker Compose


## Setup and Running the Application

1. **Clone the repository**:

   ```bash
   git clone https://github.com/chaosishere/FlaskUserCRUD.git
   cd FlaskUserCRUD

2. **Running on Docker**:

   ```bash
   docker-compose build
   docker-compose up
   
3. **Running on local**:

   ```bash
   python -m venv venv
   venv/bin/activate
   pip install -r requirements.txt
   flask run
4. **Access the application:**

   ```bash
   http://localhost:5000

## POST request body:
   ```bash
   {
  "name": "John Doe Updated",
  "email": "john.doe.updated@example.com",
  "password": "newpassword"
   }
