name = str(input('Digite seu nome completo: ')).strip()
separa = name.split()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {name.upper()}')
print(f'Seu nome em minúsculas é {name.lower()}')
print(f'Seu nome tem ao todo {len(name)-name.count(' ')} letras')
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')

# name.find(' ') -- Pode ser usado esse comando tbm para identificar o tanto de letras do primeiro nome