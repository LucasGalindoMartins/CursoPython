import math

ang = float(input('Valor do ângulo: '))
rad = math.radians(ang)

cos = math.cos(rad)
sen = math.sin(rad)
tan = math.tan(rad)

print(f'Cosseno: {round(cos, 6)}\nSeno: {round(sen, 6)}\nTangente: {round(tan, 6)}')
