import unittest
import json
from app import app

class TestAPI(unittest.TestCase):
    def test_get_categories(self):
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
