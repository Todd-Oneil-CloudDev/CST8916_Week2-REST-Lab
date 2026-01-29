class Task:
    id: int
    title: str
    description: str
    user_id: int
    completed: bool

    def __init__(self, id, title, description, user_id, completed):
        self.id = id
        self.title = title
        self.description = description
        self.user_id = user_id
        self.completed = completed
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
            "completed": self.completed
        }