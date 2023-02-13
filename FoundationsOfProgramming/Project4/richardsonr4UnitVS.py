import unittest

from richardsonr4 import Rectangle, Parallelepiped

class RectangleTest(unittest.TestCase):
    """The test class for the Rectangle class"""
    
    def setUp(self):
        """Initialize the rectangle object with width and length"""
        self.rect = Rectangle(15, 40)

    def test_perimeter(self):
        """Testing the perimeter method of the Rectangle class"""
        self.setUp()
        self.assertEqual(self.rect.perimeter(), 110)

    def test_area(self):
        """Testing the area method of the Rectangle class"""
        self.setUp()
        self.assertEqual(self.rect.area(), 600)

class ParallelepipedTest(unittest.TestCase):
    """The test class for the Parallelepiped class"""
    def setUp(self):
        """Initialize the parallelepiped object with width, length, and height"""
        self.par = Parallelepiped(15, 40, 10)

    def test_volume(self):
        """Test the volume method of the Parallelepiped class"""
        self.setUp()
        self.assertEqual(self.par.volume(), 6000)

if __name__ == "__main__":
    unittest.main()