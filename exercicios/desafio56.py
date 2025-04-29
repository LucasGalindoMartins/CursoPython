maisvelho = 0
nomemaisvelho = ''
s = 0
contmulher = 0

for p in range(1, 5):
    print(f'----- {p} PESSOA -----')
    name = input('Nome: ').strip()
    age = int(input('Idade: '))
    sex = input('Sexo [M/F]: ').strip()
    
    s += age

    if sex in 'Mm':
        if maisvelho < age:
            maisvelho = age
            nomemaisvelho = name

    if sex in 'Ff' and age < 20:
        contmulher += 1

media = s/4

print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maisvelho} anos e se chama {nomemaisvelho}.')
print(f'Ao todo são {contmulher} mulheres com menos de 20 anos.')