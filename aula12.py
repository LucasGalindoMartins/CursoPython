name = str(input('Qual é o seu nome? '))
name = name.upper()

if name == 'LUCAS':
    print(f'{name}, que nome bonito!!')

elif name == 'PEDRO' or name == 'GUSTAVO' or name == 'THIAGO':
    print('Seu nome é bem popular no Brasil.')

elif name == 'ANA' or name == 'GIOVANA' or name == 'ELLEN':
    print('Belo nome feminino.')
    
else:
    print('Seu nome é bem comum.')

print(f'Tenha um bom dia {name}.')