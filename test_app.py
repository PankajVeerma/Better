import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Welcome to my API!', result.get_data(as_text=True))

    def test_get_books(self):
        result = self.app.get('/books')
        self.assertEqual(result.status_code, 200)
        self.assertIn('1984', result.get_data(as_text=True))

    # Additional tests for POST, PUT, DELETE...

if __name__ == '__main__':
    unittest.main()
