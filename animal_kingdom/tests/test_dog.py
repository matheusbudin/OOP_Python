import unittest
from animals.dog import Dog

class TestDog(unittest.TestCase):
    def test_dog_sound(self):
        dog = Dog()
        self.assertEqual(dog.make_sound(), "Bark")

if __name__ == '__main__':
    unittest.main()
