valores = []
while True:
    valores.append(int(input('Digite um valor: ')))

    r = ' '
    while r not in 'NnSs':
        r = input('Quer continuar? [S/N]').upper()
    if r == 'N':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('O valor 5 FAZ parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')