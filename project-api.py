from flask import Flask, jsonify, abort, make_response, request
from Project import Project

projects_id_counter = 0

'''
projects = [
    {
        "project_name": "First Project",
        "id": 1,
        "state": "In progress",
        "tasks": [
            {
                "task_name": "Name",
                "task_id": 1,
                "description": "Description task 1"
            },
            {
                "task_name": "Name 2",
                "task_id": 2,
                "description": "Description task 2"
            }
        ]
    },
    {
        "project_name": "Second Project",
        "id": 2,
        "state": "In progress",
        "tasks": [
            {
                "task_name": "Name",
                "task_id": 1,
                "description": "Description task 1"
            },
            {
                "task_name": "Name 2",
                "task_id": 2,
                "description": "Description task 2"
            }
        ]
    },
    {
        "project_name": "Third Project",
        "id": 3,
        "state": "In progress",
        "tasks": [
            {
                "task_name": "Name",
                "task_id": 1,
                "description": "Description task 1"
            },
            {
                "task_name": "Name 2",
                "task_id": 2,
                "description": "Description task 2"
            }
        ]
    }
]
'''

projects = []

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to your 'Tasks for Projects'."

@app.route("/projects", methods=["GET"])
def get_projects():
    response = []
    for project in projects:
        response.append(project.to_json())
    return jsonify({"projects": response})

@app.route("/projects/<int:id>", methods=["GET"])
def get_project_by_id(id):
    for project in projects:
        if project.id == id:
            return jsonify({"project": project.to_json()})
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"project": "Not Found"}), 404)

@app.route("/projects/<int:id>", methods=["DELETE"])
def delete_project(id):
    for project in projects:
        if project.id == id:
            projects.remove(project)
            return jsonify({"project_state": "Deleted"})
    abort(404)

@app.route("/projects", methods=["POST"])
def create_project():
    global projects_id_counter

    if not request.json or not "project_name" in request.json:
        abort(400)
    project_name = request.json.get("project_name")
    projects_id_counter += 1
    state = "In progress"
    project = Project(projects_id_counter, project_name, state)
    projects.append(project)
    return jsonify({"created_new_project": project.to_json()})

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify("The request is incomplete."), 400)

@app.route("/projects/<int:id>", methods=["PUT"])
def modify_project(id):
    for project in projects:
        if project.id == id:
            project.name = request.json.get("project_name", project.name)
            project.state = request.json.get("state", project.state)
            return jsonify({"project_modified": project.to_json()})
    abort(404)

@app.route("/projects/tasks", methods=["GET"])
def get_all_tasks():
    all_tasks = []
    for project in projects:
        all_tasks.append({project["project_name"]: project["tasks"]})
    return jsonify(all_tasks)

@app.route("/projects/<int:id>/tasks", methods=["GET"])
def get_tasks_from_a_project(id):
    for project in projects:
        if project["id"] == id:
            return jsonify({project["project_name"]: project["tasks"]})
    abort(404)

@app.route("/projects/<int:id>/tasks", methods=["POST"])
def post_task(id):
    if not "task_name" in request.json:
        abort(400)

    if not "description" in request.json:
        abort(400)

    for project in projects:
        if project["id"] == id:
            task_name = request.json.get("task_name")
            id = project["tasks"][-1].get("id") + 1
            description = request.json.get("description")
            task = {"task_name": task_name, "id": id, "description": description}
            project["tasks"].append(task)
            return jsonify({project["project_name"]: project["tasks"]})

@app.route("/projects/<int:id>/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(id, task_id):
    for project in projects:
        if project["id"] == id:
            for task in project["tasks"]:
                if task["task_id"] == task_id:
                    project["tasks"].remove(task)
                    return jsonify({"task_state": "Deleted"})
    abort(404)

@app.route("/projects/<int:id>/tasks/<int:task_id>", methods=["PUT"])
def modify_task(id, task_id):
    for project in projects:
        if project["id"] == id:
            for task in project["tasks"]:
                if task["task_id"] == task_id:
                    task["task_name"] = request.json.get("task_name", task["task_name"])
                    task["description"] = request.json.get("description", task["description"])
                    return jsonify({"task_modified": task})
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)
