# Student CRUD REST API

A simple, beginner-friendly CRUD (Create, Read, Update, Delete) REST API built using Python and the Flask framework. The API uses an in-memory Python list to store student data, features comprehensive input validation, and returns all responses in JSON format.

## Project Structure

```text
CRUD_API/
│
├── app.py              # Main Flask application containing routing and validation logic
├── requirements.txt    # Project dependencies (Flask)
├── README.md           # Instructions on setup, running, and testing the API
└── test.http           # Sample HTTP requests for testing with VS Code REST Client
```

---

## Data Model

Each **Student** object is structured as follows:

| Field    | Type    | Description                      |
| :------- | :------ | :------------------------------- |
| `id`     | Integer | Unique identifier for the student|
| `name`   | String  | Name of the student (non-empty)  |
| `course` | String  | Enrolled course (non-empty)      |

---

## Installation & Setup

Ensure you have Python installed on your system.

1. **Clone or navigate** to the project directory:
   ```bash
   cd CRUD_1
   ```

2. **Install the dependencies**:
   ```bash
   py -m pip install -r requirements.txt
   ```

---

## Running the Application

To start the Flask development server (with Debug Mode enabled):

```bash
py app.py
```

By default, the server runs on `http://127.0.0.1:5000/`.

---

## API Endpoints Reference

### 1. Root Status
* **Endpoint**: `GET /`
* **Response Status**: `200 OK`
* **Response Body**:
  ```json
  {
    "message": "Student CRUD API is running"
  }
  ```

### 2. Get All Students
* **Endpoint**: `GET /students`
* **Response Status**: `200 OK`
* **Response Body**:
  ```json
  [
    { "id": 1, "name": "Alice Smith", "course": "Computer Science" },
    { "id": 2, "name": "Bob Jones", "course": "Mathematics" }
  ]
  ```

### 3. Get Student by ID
* **Endpoint**: `GET /students/<id>`
* **Success Response Status**: `200 OK`
* **Success Response Body**:
  ```json
  { "id": 1, "name": "Alice Smith", "course": "Computer Science" }
  ```
* **Error Response Status**: `404 Not Found` (If student ID does not exist)
* **Error Response Body**:
  ```json
  { "error": "Student with ID 999 not found" }
  ```

### 4. Create Student
* **Endpoint**: `POST /students`
* **Headers**: `Content-Type: application/json`
* **Request Body**:
  ```json
  {
    "id": 3,
    "name": "Charlie Brown",
    "course": "Physics"
  }
  ```
* **Success Response Status**: `201 Created`
* **Error Scenarios**:
  * Missing Fields or Invalid JSON -> `400 Bad Request`
  * Duplicate ID -> `400 Bad Request`

### 5. Update Student
* **Endpoint**: `PUT /students/<id>`
* **Headers**: `Content-Type: application/json`
* **Request Body**:
  ```json
  {
    "name": "Charlie Brown Jr.",
    "course": "Astrophysics"
  }
  ```
* **Success Response Status**: `200 OK`
* **Error Scenarios**:
  * Student Not Found -> `404 Not Found`
  * Missing Fields or Invalid JSON -> `400 Bad Request`

### 6. Delete Student
* **Endpoint**: `DELETE /students/<id>`
* **Success Response Status**: `200 OK`
* **Success Response Body**:
  ```json
  { "message": "Student with ID 3 has been deleted" }
  ```
* **Error Response Status**: `404 Not Found` (If student ID does not exist)

---

## Testing the API

### Method A: VS Code REST Client (Recommended)
1. Install the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) in VS Code.
2. Open the [test.http](file:///c:/Users/Rajani%20Kant%20Sinha/CRUD_1/test.http) file.
3. Click the `Send Request` hyperlink above any of the requests to test the endpoint.

### Method B: curl Commands
You can also run testing commands from your terminal (make sure the app is running):
* **Get All Students**:
  ```bash
  curl -X GET http://127.0.0.1:5000/students
  ```
* **Create a Student**:
  ```bash
  curl -X POST http://127.0.0.1:5000/students -H "Content-Type: application/json" -d "{\"id\": 3, \"name\": \"Charlie Brown\", \"course\": \"Physics\"}"
  ```
