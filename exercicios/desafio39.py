from datetime import date

nasc = int(input('Ano de nascimento: '))
ano = date.today().year
age = ano - nasc

print(f'Quem nasceu em {nasc} tem {age} anos em {ano}.')

if age < 18:
    print(f'Ainda faltam {18 - age} anos para o alistamento.')
    print(f'Seu alistamento será em {(18 - age) + ano}.')
elif age > 18:
    print(f'Você já deveria ter se alistado há {age - 18} anos.')
    print(f'Seu alistamento foi em {ano - (age - 18)}.')
elif age == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!')