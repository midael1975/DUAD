import json
from flask import Flask, request, jsonify

app = Flask(__name__)

FILE_PATH = "tareas.json"
VALID_STATUS = ["to_do", "in_progress", "completed"]


# ---------------------------
# Helper functions
# ---------------------------

def read_tasks():
    """Read tasks from the JSON file."""
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []


def write_tasks(tasks):
    """Write tasks to the JSON file."""
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)


# ---------------------------
# GET - Retrieve tasks (optional status filter)
# ---------------------------
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = read_tasks()
    status_filter = request.args.get("status")

    if status_filter:
        if status_filter not in VALID_STATUS:
            return jsonify({"error": "Invalid status"}), 400

        tasks = [t for t in tasks if t["status"] == status_filter]

    return jsonify(tasks)


# ---------------------------
# POST - Create a new task
# ---------------------------
@app.route('/tasks', methods=['POST'])
def create_task():
    tasks = read_tasks()
    data = request.get_json()

    # Validations
    if "id" not in data:
        return jsonify({"error": "Task must have an id"}), 400

    if any(t["id"] == data["id"] for t in tasks):
        return jsonify({"error": "Task id already exists"}), 400

    if not data.get("title"):
        return jsonify({"error": "Task must have a title"}), 400

    if not data.get("description"):
        return jsonify({"error": "Task must have a description"}), 400

    if not data.get("status"):
        return jsonify({"error": "Task must have a status"}), 400

    if data["status"] not in VALID_STATUS:
        return jsonify({"error": "Invalid status"}), 400

    # Create task
    new_task = {
        "id": data["id"],
        "title": data["title"],
        "description": data["description"],
        "status": data["status"]
    }

    tasks.append(new_task)
    write_tasks(tasks)

    return jsonify(new_task), 201


# ---------------------------
# PUT - Update a task
# ---------------------------
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = read_tasks()
    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:

            # Validate status if provided
            if "status" in data and data["status"] not in VALID_STATUS:
                return jsonify({"error": "Invalid status"}), 400

            # Update fields
            task["title"] = data.get("title", task["title"])
            task["description"] = data.get("description", task["description"])
            task["status"] = data.get("status", task["status"])

            write_tasks(tasks)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


# ---------------------------
# DELETE - Remove a task
# ---------------------------
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = read_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            write_tasks(tasks)
            return jsonify({"message": "Task deleted"})

    return jsonify({"error": "Task not found"}), 404


# ---------------------------
# RUN
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
