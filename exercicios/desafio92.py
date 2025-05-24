from datetime import datetime
funcionario = {}
funcionario['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
funcionario['idade'] = datetime.now().year - nasc
funcionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if funcionario['ctps'] == 0:
    print('-='*30)
    for k, v in funcionario.items():
        print(f'- {k} tem valor {v}')
else:
    funcionario['contratação'] = int(input('Ano de Contratação: '))
    funcionario['salario'] = float(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['idade'] + ((funcionario['contratação'] + 35) - datetime.now().year)
    print('-='*30)
    for k, v in funcionario.items():
        print(f'- {k} tem o valor {v}')
