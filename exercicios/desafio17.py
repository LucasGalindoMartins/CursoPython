from math import sqrt
co = float(input('Digite o cateto oposto do triângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo: '))
hip = (co**2) + (ca**2)
print(f'A hipotenusa desse triângulo é {sqrt(hip)}')