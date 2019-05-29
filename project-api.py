from flask import Flask, jsonify

projects = [
    {"Project 1": "task 1"},
    {"Project 2": "task 2"},
    {"Project 3": "task 3"}
]

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to your 'Tasks for Projects'."

@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify({"PROJECTS": projects})

if __name__ == "__main__":
    app.run(debug=True)
