class Task(object):

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.completed = False

    def to_json(self):
        return {
            "id": self.id,
            "task_name": self.name,
            "description": self.description
        }