# valores = []
# valores.append(int(input('Digite um valor: ')))
# print('Valor adicionado com sucesso...')

# while True:
#     r = ' '
#     while r not in 'SN':
#         r = input('Quer continuar? [S/N]').strip().upper()[0]
#     if r == 'N':
#         break

#     val = int(input('Digite um valor: '))
#     if val in valores:
#         print('Valor duplicado! Não vou adicionar...')
#     else:
#         print('Valor adicionado com sucesso...')
#         valores.append(val)
# print('-='*30)
# valores.sort()
# print(f'Você digitou os valores {valores}')


# COM O PROFESSOR
numeros = []
while True:
    n = int(input('Digite um valor: '))

    if n in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        numeros.append(n)

    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]').strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

