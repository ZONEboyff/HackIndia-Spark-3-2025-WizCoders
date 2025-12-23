# src/storage.py
from hyperon import MeTTa

class TaskStorage:
    """Handles persistent storage and retrieval of tasks using MeTTa."""
    def __init__(self, metta_file='task.metta'):
        self.metta_file = metta_file
        self.metta = MeTTa()

    def load(self):
        with open(self.metta_file, 'r') as f:
            self.metta.run(f.read())

    def save(self):
        result = self.metta.space().get_atoms()
        with open(self.metta_file, 'w') as f:
            for atom in result:
                f.write(str(atom) + '\n')

    def get_metta(self):
        return self.metta
