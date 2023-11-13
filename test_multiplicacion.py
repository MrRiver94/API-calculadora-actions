import unittest
from multiplicacion import multiplicar

class Testmultiplicar(unittest.TestCase):
     def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 4), -4)
        self.assertEqual(multiplicar(-2, -8), 16)
if __name__ == '__main__':
 unittest.main()