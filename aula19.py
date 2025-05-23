# pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 19}
# print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# del pessoas['sexo']
# pessoas['nome'] = 'Gustavo'
# pessoas['peso'] = 60

# for k in pessoas.keys():
#     print(k)

# for k in pessoas.values():
#     print(k)

# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 =  {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[0]['uf'])
# print(brasil[0]['sigla'])

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    # for k, v in e.items():
    #     print(f'O campo {k} tem valor {v}')
    for v in e.items():
        print(v, end=' ')
    print()