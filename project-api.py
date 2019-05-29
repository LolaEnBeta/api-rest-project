from flask import Flask, jsonify, abort, make_response, request

projects = [
    {"ProjectName": "First Project",
    "id": 1,
    "state": "In progress",
    "tasks": [
            {"taskName": "Name",
            "id": 1,
            "description": "Description task 1"},

            {"taskName": "Name 2",
            "id": 2,
            "description": "Description task 2"}
            ]
    },

    {"ProjectName": "Second Project",
    "id": 2,"state": "In progress",
    "tasks": [
            {"taskName": "Name",
            "id": 1,
            "description": "Description task 1"},

            {"taskName": "Name 2",
            "id": 2,
            "description": "Description task 2"}
            ]
    },

    {"ProjectName": "Third Project",
    "id": 3,
    "state": "In progress",
    "tasks": [
            {"taskName": "Name",
            "id": 1,
            "description": "Description task 1"},

            {"taskName": "Name 2",
            "id": 2,
            "description": "Description task 2"}
            ]
    }
]

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to your 'Tasks for Projects'."

@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify({"PROJECTS": projects})

@app.route("/projects/<int:id>", methods=["GET"])
def get_one_project(id):
    for project in projects:
        for task in project:
            if project["id"] == id:
                return jsonify({"project": project})
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"Project": "Not Found"}), 404)

@app.route("/projects/<int:id>", methods=["DELETE"])
def delete_project(id):
    for project in projects:
        if project["id"] == id:
            projects.remove(project)
            return jsonify({"Project state": "Deleted"})
    abort(404)

@app.route("/projects", methods=["POST"])
def post_project():
    if not request.json or not "ProjectName" in request.json:
        abort(400)
    ProjectName = request.json.get("ProjectName")
    id = projects[-1].get("id") + 1
    state = "In progress"
    tasks = "You need to add a task in this project."

    projects.append({"ProjectName": ProjectName, "id": id, "state": state, "tasks": tasks})
    return jsonify({"ProjectName": ProjectName, "id": id, "state": state, "tasks": tasks})

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify("You need to name the project."), 400)

@app.route("/projects/<int:id>", methods=["PUT"])
def put_project(id):
    for project in projects:
        if project["id"] == id:
            project["ProjectName"] = request.json.get("ProjectName", project["ProjectName"])
            project["state"] = request.json.get("state", project["state"])
            project["tasks"] = request.json.get("tasks", project["tasks"])
            return jsonify({"Project modified": project})
    abort(404)

@app.route("/projects/tasks", methods=["GET"])
def get_all_tasks():
    all_tasks = []
    for project in projects:
        all_tasks.append({project["ProjectName"]: project["tasks"]})
    return jsonify(all_tasks)

@app.route("/projects/<int:id>/tasks", methods=["GET"])
def get_tasks_from_a_project(id):
    for project in projects:
        if project["id"] == id:
            return jsonify({project["ProjectName"]: project["tasks"]})
    abort(404)

@app.route("/projects/<int:id>/tasks", methods=["POST"])
def post_task(id):
    for project in projects:
        if project["id"] == id:
            taskName = request.json.get("taskName")
            id = project["tasks"][-1].get("id") + 1
            description = request.json.get("description")
            project["tasks"].append({"taskName": taskName, "id": id, "description": description})
            return jsonify({project["ProjectName"]: project["tasks"]})

if __name__ == "__main__":
    app.run(debug=True)
