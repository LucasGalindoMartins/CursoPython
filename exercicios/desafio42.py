n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))

if (n1 + n2 > n3) and (n2 + n3 > n1) and (n1 + n3 > n2):
    print('Os segmentos acima PODEM FORMAR um triângulo ')
    if n1 == n2 == n3:
        print('Esse triângulo é EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('Esse triângulo é ESCALENO!')
    else:
        print('Esse triângulo é ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!!')

