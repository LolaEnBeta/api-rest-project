class Project(object):

    def __init__(self, id, name, state):
        self.id = id
        self.name = name
        self.state = state

    def to_json(self):
        return {
            "id": self.id,
            "project_name": self.name,
            "state": self.state
        }