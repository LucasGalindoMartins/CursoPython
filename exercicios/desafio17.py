from math import hypot
co = float(input('Digite o cateto oposto do triângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo: '))
hip = hypot(co, ca)
print(f'A hipotenusa desse triângulo é {hip:.2f}')

# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print(f'A hipotenusa vai medir {hi:.2f}')