def sumar(a, b):
 return a + b

def restar(a, b):
 return a - b

def multiplicar(a, b):
 return a * b

def dividir(a, b):
 if b == 0:
   raise ValueError("No se puede dividir entre 0")
 
 return a / b

if __name__ == "__main__":
    print(sumar(5, 3))

if __name__ == "__main__":
    print(restar(4, 2))

if __name__ == "__main__":
    print(multiplicar(5, 5))

if __name__ == "__main__":
    print(dividir(24, 6))