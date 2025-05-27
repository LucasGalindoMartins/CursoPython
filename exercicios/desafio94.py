# dados = {}
# pessoa = []
# totidade  = []
# femeas = []
# while True:
#     dados['nome'] = input("Nome: ")

#     dados['sexo'] = input('Sexo [M/F]: ').upper()
#     while dados['sexo'] not in 'MmFf':
#         print('ERRO! Por favor, digite apenas M ou F.')
#         dados['sexo'] = input('Sexo [M/F]: ').upper()
#     if dados['sexo'] == 'F':
#         femeas.append(dados['nome'])
    
#     dados['idade'] = int(input('Idade: '))
#     totidade.append(dados['idade'])

#     pessoa.append(dados.copy())

#     r = ' '
#     r = input('Quer continuar? [S/N]').upper()
#     while r not in 'NnSs':
#         print('ERRO! Responda apenas S ou N.')
#         r = input('Quer continuar? [S/N]').upper()
#     if r == 'N':
#         break
# print('-='*30)
# print(f'A) Ao todo temos {len(pessoa)} pessoas cadastradas.')

# m = sum(totidade)/len(pessoa)
# print(f'B) A média de idade é de {m:.2f} anos.')

# print(f'C) As mulheres cadastradas foram ', end='')
# for f in femeas:
#     print(f'{f} ', end='')

# print(f'\nD) Lista de pessoas que estão acima da média de idade: ')
# for d in pessoa:
#     if d['idade'] > m:
#       for k, v in d.items():
#           print(f'{k} = {v};', end=' ')
#     print()
# print('<<  ENCERRADO  >>')

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break  
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r  = input('Quer continuar? [S/N] ').upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma/len(galera)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()

print(f'D) Lista de pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<  ENCERRADO  >>')
