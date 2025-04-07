import math

ang = float(input('Valor do ângulo: '))
rad = math.radians(ang)

cos = math.cos(rad)
sen = math.sin(rad)
tan = math.tan(rad)

print(f'Cosseno: {cos:.2f}\nSeno: {sen:.2f}\nTangente: {tan:.2f}')
