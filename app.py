from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data stored in an in-memory Python list
students = [
    {"id": 1, "name": "Alice Smith", "course": "Computer Science"},
    {"id": 2, "name": "Bob Jones", "course": "Mathematics"}
]

@app.route('/', methods=['GET'])
def index():
    """
    GET /
    Returns a simple message confirming that the API is running.
    """
    return jsonify({"message": "Student CRUD API is running"}), 200

@app.route('/ui', methods=['GET'])
def ui():
    """
    GET /ui
    Renders the frontend HTML page for the Student CRUD API.
    """
    return render_template('index.html'), 200

@app.route('/students', methods=['GET'])
def get_students():
    """
    GET /students
    Returns the complete list of students.
    """
    return jsonify(students), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    GET /students/<id>
    Returns a single student by their ID.
    If not found, returns HTTP 404 with an error message.
    """
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": f"Student with ID {student_id} not found"}), 404
    return jsonify(student), 200

@app.route('/students', methods=['POST'])
def create_student():
    """
    POST /students
    Accepts JSON input to add a new student.
    Validates that 'id', 'name', and 'course' are provided, types are correct,
    and the 'id' is not a duplicate.
    Returns HTTP 201 on success.
    """
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json()

    # Field presence validation
    required_fields = ["id", "name", "course"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: '{field}'"}), 400

    student_id = data["id"]
    name = data["name"]
    course = data["course"]

    # Data type validation
    if not isinstance(student_id, int):
        return jsonify({"error": "Field 'id' must be an integer"}), 400
    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Field 'name' must be a non-empty string"}), 400
    if not isinstance(course, str) or not course.strip():
        return jsonify({"error": "Field 'course' must be a non-empty string"}), 400

    # Duplicate ID check
    if any(s["id"] == student_id for s in students):
        return jsonify({"error": f"Student with ID {student_id} already exists"}), 400

    # Create new student and append
    new_student = {
        "id": student_id,
        "name": name.strip(),
        "course": course.strip()
    }
    students.append(new_student)

    return jsonify(new_student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    PUT /students/<id>
    Updates an existing student's name and course.
    Returns HTTP 200 on success.
    Returns HTTP 404 if the student does not exist.
    """
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": f"Student with ID {student_id} not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json()

    # Field presence validation
    required_fields = ["name", "course"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: '{field}'"}), 400

    name = data["name"]
    course = data["course"]

    # Data type validation
    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Field 'name' must be a non-empty string"}), 400
    if not isinstance(course, str) or not course.strip():
        return jsonify({"error": "Field 'course' must be a non-empty string"}), 400

    # Update values
    student["name"] = name.strip()
    student["course"] = course.strip()

    return jsonify(student), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    DELETE /students/<id>
    Deletes a student by ID.
    Returns HTTP 200 on success.
    Returns HTTP 404 if the student does not exist.
    """
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        return jsonify({"error": f"Student with ID {student_id} not found"}), 404

    students.remove(student)
    return jsonify({"message": f"Student with ID {student_id} has been deleted"}), 200

# Error handlers to ensure JSON response format for general app errors
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed"}), 405

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Enable Flask debug mode as required
    app.run(debug=True)
