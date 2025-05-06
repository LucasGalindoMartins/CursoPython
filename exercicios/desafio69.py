age = cage = cmen = cwomen = 0
r = ' '

while True:
  print('-'*30)
  print('CADASTRE UMA PESSOA')
  print('-'*30)

  age = int(input('Idade: '))
  if age > 18:
    cage += 1

  sex = ' '
  while sex not in 'MF':
    sex = input('Sexo: [M/F]').strip().upper()[0]
  if sex == 'M':
    cmen += 1
  elif sex == 'F' and age < 20:
    cwomen += 1

  r = ' '
  print('-'*30)
  while r not in 'SN':
    r = input('Quer continuar? [S/N]').strip().upper()[0]
  if r == 'N':
    break
print(f'Total de pessoas com mais de 18 anos: {cage}')
print(f'Homens cadastrados: {cmen}')
print(f'Mulheres com menos de 20 anos: {cwomen}')
