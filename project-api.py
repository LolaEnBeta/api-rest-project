from flask import Flask, jsonify, abort, make_response

projects = [
    {"ProjectName": "First Project",
    "id": 1},
    {"ProjectName": "Second Project",
    "id": 2},
    {"ProjectName": "Third Project",
    "id": 3}
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

if __name__ == "__main__":
    app.run(debug=True)
