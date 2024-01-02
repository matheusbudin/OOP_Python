import unittest
from users.user import User

class TestUser(unittest.TestCase):
    def test_user_initialization(self):
        user = User("John Doe", "john@example.com")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")

if __name__ == '__main__':
    unittest.main()
