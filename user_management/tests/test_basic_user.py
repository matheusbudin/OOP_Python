import unittest
from users.basic_user import BasicUser

class TestBasicUser(unittest.TestCase):
    def test_basic_user(self):
        user = BasicUser("Jane Doe", "jane@example.com")
        self.assertEqual(user.display_info(), "User: Jane Doe, Email: jane@example.com, Type: Basic")

if __name__ == '__main__':
    unittest.main()
