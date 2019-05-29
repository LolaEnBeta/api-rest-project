from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)
