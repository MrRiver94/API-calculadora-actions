import unittest
from division import dividir

class Testdividir(unittest.TestCase):
     def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(2, 5), 0.4)
        self.assertEqual(dividir(8, 0)," Error")
if __name__ == '__main__':
 unittest.main()