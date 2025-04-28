from datetime import date

atual = date.today().year
age = 0
menor = 0
maior = 0

for p in range(1, 8):
    nasc = int(input(f'Em que ano a {p} pessoa nasceu? '))
    age = atual - nasc
    if age < 18:
        menor += 1
    elif age >= 18:
        maior += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade.\nE também tivemos {menor} pessoas menores de idade.')


