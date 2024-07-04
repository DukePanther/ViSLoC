import unittest
from app.ai_module import get_advice

class TestAIModule(unittest.TestCase):
    def test_get_advice(self):
        result = get_advice("What is Python?")
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()