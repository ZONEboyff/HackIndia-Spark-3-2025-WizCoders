import unittest
from src.task_model import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        t = Task("Test", "2025-12-31", 5)
        self.assertEqual(t.name, "Test")
        self.assertEqual(t.deadline, "2025-12-31")
        self.assertEqual(t.priority, 5)

if __name__ == "__main__":
    unittest.main()
