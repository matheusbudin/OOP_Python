import unittest
from animals.animal import Animal

class TestAnimal(unittest.TestCase):
    def test_animal_sound(self):
        animal = Animal()
        self.assertEqual(animal.make_sound(), "Some generic sound")

if __name__ == '__main__':
    unittest.main()
