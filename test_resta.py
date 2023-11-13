import unittest
from resta import restar

class TestRestar(unittest.TestCase):
     def test_restar(self):
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(-1, 5), 4)
        self.assertEqual(restar(-1, -4), 3)
if __name__ == '__main__':
 unittest.main()