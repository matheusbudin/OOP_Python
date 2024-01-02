import unittest
from users.premium_user import PremiumUser

class TestPremiumUser(unittest.TestCase):
    def test_premium_user(self):
        user = PremiumUser("Alice Smith", "alice@example.com")
        self.assertEqual(user.display_info(), "User: Alice Smith, Email: alice@example.com, Type: Premium, Premium Features: Enabled")

if __name__ == '__main__':
    unittest.main()
