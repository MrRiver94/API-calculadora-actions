import unittest
from operaciones import sumar, restar, multiplicar ,dividir

class TestSumar(unittest.TestCase):
     def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
if __name__ == '__main__':
 unittest.main()

 class TestRestar(unittest.TestCase):
     def test_restar(self):
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(-1, 5), 4)
        self.assertEqual(restar(-1, -4), 3)
if __name__ == '__main__':
 unittest.main()

 class Testmultiplicar(unittest.TestCase):
     def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 4), -4)
        self.assertEqual(multiplicar(-2, -8), 16)
if __name__ == '__main__':
 unittest.main()

 class Testdividir(unittest.TestCase):
     def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(9, 3), 0.4)
        with self.assertRaises(ValueError):
                dividir(8, 0)
if __name__ == '__main__':
 unittest.main()