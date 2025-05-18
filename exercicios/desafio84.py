# MINHA RESOLUÇÃO
# dado = []
# pessoas = []
# contp = maior = 0
# pessoaleve = []
# pessoapesada  =  []
# while True:
#     dado.append(input('Nome: '))
#     dado.append(float(input('Peso: ')))
#     pessoas.append(dado[:])
#     dado.clear()
#     contp += 1

#     r = ' '
#     while r not in 'NnSs':
#         r = input('Quer continuar? [S/N]').upper()
#     if r == 'N':
#         break
# print('-='*30)
# print(f'Ao todo, você cadastrou {contp} pessoas.')
# menor = pessoas[1][1]
# for p in pessoas:
#     if p[1] >= maior:
#         maior = p[1]
#     if p[1] <= menor:
#         menor = p[1]

# for p in pessoas:
#     if p[1] == maior:
#         pessoapesada.append(p[0])
#     if p[1] == menor:
#         pessoaleve.append(p[0])

# print(f'O maior peso foi de {maior}Kg. Peso de {pessoapesada}')
# print(f'O menor peso foi de {menor}Kg. Peso de {pessoaleve}')

# COM O PROFESSOR
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor =  temp[1]
    princ.append(temp[:])
    temp.clear()

    r = ' '
    while r not in 'NnSs':
        r = input('Quer continuar? [S/N]').upper()
    if r == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')