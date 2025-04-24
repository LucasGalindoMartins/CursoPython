from datetime import date

bor = int(input('Digite o ano que nasceu: '))
y = date.today().year
age = y - bor

print(f'O atleta tem {age} anos.')

if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Classificação: INFANTIL')
elif age <= 19:
    print('Classificação: JUNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')