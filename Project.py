class Project(object):

    def __init__(self, id, name, state):
        self.id = id
        self.name = name
        self.state = state
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_json(self):
        tasks_json = [task.to_json() for task in self.tasks]

        return {
            "id": self.id,
            "project_name": self.name,
            "state": self.state,
            "tasks": tasks_json
        }
