from flask import Flask, jsonify, abort, make_response, request

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

@app.route("/projects", methods=["POST"])
def post_project():
    if not request.json or not "ProjectName" in request.json:
        abort(400)
    ProjectName = request.json.get("ProjectName")
    id = projects[-1].get("id") + 1

    projects.append({"ProjectName": ProjectName, "id": id})
    return jsonify({"ProjectName": ProjectName, "id": id})

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify("You need to name the project."), 400)

if __name__ == "__main__":
    app.run(debug=True)
