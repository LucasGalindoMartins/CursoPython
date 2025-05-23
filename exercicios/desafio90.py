aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
if aluno['media'] < 6:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Recuperação'
print('-='*30)
# print(f'- nome é igual a {aluno['nome']}')
# print(f'- média é igual a {aluno['media']}')
# print(f'- situação é igual a {aluno["situ"]}')

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
