import unittest

from richardsonr3 import isGameOver

class GameOverTest(unittest.TestCase):
    
    def test_isGameOver(self):
        grid = [['X' for j in range(10)] for i in range(10)]
        self.assertTrue(isGameOver(grid))
    
    def test_not_game_over(self):
        grid = [['S' for j in range(10)] for i in range(10)]
        self.assertFalse(isGameOver(grid))
        


if __name__ == "__main__":
    unittest.main()

