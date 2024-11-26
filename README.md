# Parcel Management System

A Django-based backend system to manage parcels, brokers, and offers, with authentication using a token-based system and environment-based configuration using `.env` files.

## Features

- **Manage Parcels, Brokers, and Offers Using a RESTful API:**
  - Create, update, delete, and retrieve parcels, brokers, and offers.
  - Supports filtering, pagination, and sorting for brokers, parcels, and offers.

- **Authentication:**
  - All endpoints are protected using token-based authentication.
  - Tokens are specified in the `.env` file and validated before accessing any API.

- **Background Job:**
  - A background job monitors parcels grouped by block and subdivision.
  - Sends notifications (POST to a dummy API) when all parcels in a specific block and subdivision have active offers.

- **Secure Environment Variable Management:**
  - `.env` file is used to securely store sensitive environment variables (e.g., database credentials, API tokens).

- **Database Seeded with Initial Data:**
  - Predefined lookup tables:
    - **Land Use Groups**: `Agricultural`, `Residential`, `Commercial`.
    - **Broker Types**: `Personal`, `Company`, `Governmental`.
  - Includes sample parcels and brokers for testing.

- **Unit Tests:**
  - Comprehensive unit tests for all API endpoints:
    - Ensures the correct behavior for CRUD operations.
    - Validates authentication and authorization logic.
  - Tests for database integrity:
    - Ensures data is stored and retrieved correctly.
  - Test coverage reports to ensure code quality.

- **Filter, Search, and Pagination:**
  - All listing APIs (brokers, parcels, offers) support:
    - Filtering by specific fields (e.g., block number, subdivision number, price per meter).
    - Search by keywords in relevant fields (e.g., name, description).
    - Pagination with configurable page size and ordering.

- **Error Handling:**
  - Consistent error responses for all APIs (e.g., `400 Bad Request`, `401 Unauthorized`, `404 Not Found`).
  - Validates incoming data to ensure clean and predictable API behavior.

- **Easy Deployment:**
  - Ready-to-run project with minimal setup:
    - Docker support for containerized deployment (optional).
    - Instructions for running locally or on production environments.

---

## Architecture

![Parcel Management System](https://i.ibb.co/P1j8j4C/parcel-offers-management.png)

---

## Prerequisites

Ensure the following are installed:
- Python (Preferably 3.0 or higher)
- pip (Python package manager)
- PostgreSQL

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:RyadPasha/parcel-management-system.git
cd parcel-management-system
```

### 2. Create a Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database
  Create the database and user in PostgreSQL:
  ```sql
  CREATE DATABASE parcel_management;
  CREATE USER parcel_user WITH PASSWORD 'parcel_password';
  GRANT ALL PRIVILEGES ON DATABASE parcel_management TO parcel_user;
  ```

### 5. Configure Environment Variables
  1. Rename the `.env.example` file to `.env`:
  ```bash
  cp .env.example .env
  ```

   2. Update the `.env` file with your values:
  ```makefile
  # ====================
  # DATABASE CONFIGURATION
  # ====================
  DB_NAME=                          # Database name
  DB_USER=                          # Database username
  DB_PASSWORD=                      # Database password
  DB_HOST=                          # Database host (e.g., localhost, or a server IP/URL)
  DB_PORT=                          # Database port (default for PostgreSQL: 5432)

  # ====================
  # APPLICATION SETTINGS
  # ====================
  NOTIFICATION_SERVICE_API_URL=     # Example: "https://dummyjson.com/http/200/notify"
  SECRET_KEY=                       # Secret key for the application (use a strong, secure key)
  DEBUG=                            # Debug mode (True for development, False for production)
  ENV=                              # Application environment (e.g., development, production)
  ```

### 6. Run Migrations
  Apply migrations to create the database schema:
  ```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

### 7. Seed the Database
  Seed initial lookup data (Land Use Groups, Broker Types and Parcel Data):
  ```bash
  python3 manage.py seed_data
  ```

### 8. Start the Job to Monitor Parcels
  Start the worker to monitor parcels and send notifications when all parcels in a block and subdivision have active offers
  ```bash
  python3 manage.py monitor_parcels
  ```
  This will:
  - Continuously monitor parcels.
  - Automatically send notifications to the dummy API when conditions are met.
  - Log progress in the terminal.

### 9. Start the Server
  Start the development server:
  ```bash
  python3 manage.py runserver
  ```
  The API will be accessible at `http://127.0.0.1:8000`.

---

## Authentication

### Token-Based Authentication
- Add the authentication token to your `.env` file:
```
SECRET_KEY=development-secret-key
```

- Include the token in the Authorization header for all API requests:
```
Authorization: Bearer development-secret-key
```

---

## API Endpoints

### Parcels

1. **Add Parcel**
   - Endpoint: `POST /api/parcels`
   - Payload:
     ```json
     {
         "block_number": 202,
         "neighbourhood": "Al Malaz",
         "subdivision_number": 3,
         "land_use_group": 2,
         "description": "A residential parcel in Al Malaz, Riyadh, ideal for housing development."
     }
     ```
   - Response:
     ```json
     {
         "id": 1,
         "message": "Success"
     }
     ```
   - Curl Command:
     ```bash
     curl -X POST http://127.0.0.1:8000/api/parcels \
     -H "Authorization: Bearer development-secret-key" \
     -H "Content-Type: application/json" \
     -d '{"block_number": 202, "neighbourhood": "Al Malaz", "subdivision_number": 3, "land_use_group": 2, "description": "A residential parcel in Al Malaz, Riyadh, ideal for housing development."}'
     ```

2. **Get All Parcels**
   - Endpoint: `GET /api/parcels`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/parcels \
    -H "Authorization: Bearer development-secret-key"
    ```

3. **Get All Parcels with Filters**
   - Endpoint: `GET /api/parcels`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/parcels?block_number=12&land_use_group=3&ordering=-creation_date&page=1 \
    -H "Authorization: Bearer development-secret-key"
    ```

4. **Get Parcel by ID**
   - Endpoint: `GET /api/parcels/<id>`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/parcels/1/ \
    -H "Authorization: Bearer development-secret-key"
    ```

---

### Brokers

1. **Add Broker**
   - Endpoint: `POST /api/brokers`
   - Payload:
     ```json
     {
         "name": "Abdullah Al Harbi",
         "type": 2,
         "phone_number": "0501234567",
         "email": "abdullah.alharbi@realestate.sa",
         "address": "King Fahd Road, Riyadh",
         "bio": "A broker with expertise in commercial properties across Saudi Arabia."
     }
     ```
   - Response:
     ```json
     {
         "id": 1,
         "message": "Success"
     }
     ```
   - Curl Command:
     ```bash
     curl -X POST http://127.0.0.1:8000/api/brokers \
     -H "Authorization: Bearer development-secret-key" \
     -H "Content-Type: application/json" \
     -d '{"name": "Abdullah Al Harbi", "type": 2, "phone_number": "0501234567", "email": "abdullah.alharbi@realestate.sa", "address": "King Fahd Road, Riyadh", "bio": "A broker with expertise in commercial properties across Saudi Arabia."}'
     ```

2. **Get All Brokers**
   - Endpoint: `GET /api/brokers`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/brokers/ \
    -H "Authorization: Bearer development-secret-key"
    ```

3. **Get All Brokers with Filters**
   - Endpoint: `GET /api/parcels`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/brokers?type=1&search=Riyad&ordering=last_update_date&page=2 \
    -H "Authorization: Bearer development-secret-key"
    ```

4. **Get Broker by ID**
   - Endpoint: `GET /api/brokers/<id>`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/brokers/1/ \
    -H "Authorization: Bearer development-secret-key"
    ```

---

### Offers

1. **Add Offer**
   - Endpoint: `POST /api/offers`
   - Payload:
     ```json
     {
         "title": "Commercial Development in King Abdullah Economic City",
         "description": "An opportunity to develop a commercial complex in King Abdullah Economic City.",
         "broker": 1,
         "parcels": [1, 2],
         "price_per_meter": 850.50
     }
     ```
   - Response:
     ```json
     {
         "id": 1,
         "message": "Success"
     }
     ```
   - Curl Command:
     ```bash
     curl -X POST http://127.0.0.1:8000/api/offers \
     -H "Authorization: Bearer development-secret-key" \
     -H "Content-Type: application/json" \
     -d '{"title": "Commercial Development in King Abdullah Economic City", "description": "An opportunity to develop a commercial complex in King Abdullah Economic City.", "broker": 1, "parcels": [1, 2], "price_per_meter": 850.50}'
     ```

2. **Get All Offers**
   - Endpoint: `GET /api/offers`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/offers/ \
    -H "Authorization: Bearer development-secret-key"
    ```

3. **Get All Offers with Filters**
   - Endpoint: `GET /api/offers`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/offers?price_per_meter=100&ordering=-price_per_meter&page=1 \
    -H "Authorization: Bearer development-secret-key"
    ```

4. **Get Offer by ID**
   - Endpoint: `GET /api/offers/<id>`
   - Curl Command:
    ```bash
    curl -X GET http://127.0.0.1:8000/api/offers/1 \
    -H "Authorization: Bearer development-secret-key"
    ```

5. **Update Offer by ID (Partial Update [PATCH])**
   - Endpoint: `PATCH /api/offers/<offer_id>/update/`
   - Curl Command:
    ```bash
    curl -X PATCH http://127.0.0.1:8000/api/offers/1/update/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer development-secret-key" \
    -d '{
        "title": "Updated Offer Title",
        "price_per_meter": 150.75
    }'
    ```

6. **Update Offer by ID (Full Update [PUT])**
   - Endpoint: `PUT /api/offers/<offer_id>/update/`
   - Curl Command:
    ```bash
    curl -X PUT http://127.0.0.1:8000/api/offers/1/update/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer development-secret-key" \
    -d '{
        "title": "Commercial Development in King Abdullah Economic City",
        "description": "An opportunity to develop a commercial complex in King Abdullah Economic City.",
        "broker": 1,
        "parcels": [1, 2],
        "price_per_meter": 850.50
    }'
    ```

7. **Delete Offer by ID**
   - Endpoint: `DELETE /api/offers/<offer_id>/delete/`
   - Curl Command:
    ```bash
    curl -X DELETE http://127.0.0.1:8000/api/offers/1/delete/ \
    -H "Authorization: Bearer development-secret-key" \
    -H "Content-Type: application/json"
    ```

---

## Monitor Parcels
Run the background job to monitor parcels:
```bash
python3 manage.py monitor_parcels
```
This will:
- Continuously monitor parcels.
- Automatically send notifications to the dummy API when conditions are met.
- Log progress in the terminal.

---

## Running Tests

To run unit tests:
```bash
python3 manage.py test apps.parcels.tests apps.brokers.tests apps.offers.tests
```

## Contact

Created by [Mohamed Riyad](mailto:mohamed@ryad.dev).

## License

MIT License. See the [LICENSE](LICENSE) file for more information.