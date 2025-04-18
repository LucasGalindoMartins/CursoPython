print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if (n1 + n2 > n3) and (n2 + n3 > n1) and (n1 + n3 > n2):
    print('Os segmentos acima PODEM FORMAR um triângulo!!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!!')

