# src/task_model.py
class Task:
    """Encapsulates task data and operations."""
    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = deadline
        self.priority = int(priority)

    def __repr__(self):
        return f"Task(name={self.name}, deadline={self.deadline}, priority={self.priority})"

    def copy(self):
        return Task(self.name, self.deadline, self.priority)
