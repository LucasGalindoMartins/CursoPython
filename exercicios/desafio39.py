from datetime import date

sex = str(input('Digite seu sexo (H/M): '))
if sex == 'M':
    print('Você é mulher, não precisa se alistar.')
elif sex != 'M' and sex != 'H':
    print('OPÇÃO INVÁLIDA. Tente novamente.')
else:
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