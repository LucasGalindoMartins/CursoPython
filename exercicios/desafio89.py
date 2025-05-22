# dados = []
# pessoa = []
# c = 0
# while True:
#     dados.append(input('Nome: '))
#     dados.append(float(input('Nota 1: ')))
#     dados.append(float(input('Nota 2: ')))
#     m = (dados[1]+dados[2])/2
#     dados.append(m)
#     pessoa.append(dados[:])
#     dados.clear()

#     r = ' '
#     while r not in 'NnSs':
#          r = input('Quer continuar? [S/N]').upper()
#     if r == 'N':
#         break
# print('-='*30)
# print('No. NOME      MÉDIA')
# print('-'*30)
# for p in pessoa:
#     print(f'{c}  {p[0]}     {p[3]}')
#     c += 1
# print('-'*30)

# while True:
#     notas = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
#     if notas == 999:
#         print('FINALIZANDO...')
#         print('<<< VOLTE SEMPRE >>>')
#         break
#     else:
#         print(f'Notas de {pessoa[notas][0]} são [{pessoa[notas][1]}, {pessoa[notas][2]}]')
#     print('-'*30)

#COM O PROFESSOR
ficha = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2)/2
    ficha.append([nome, [n1, n2], m])

    r = ' '
    while r not in 'NnSs':
         r = input('Quer continuar? [S/N]').upper()
    if r == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'* 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')