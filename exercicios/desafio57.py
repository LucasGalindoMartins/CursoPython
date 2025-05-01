sex = input('Informe seu sexo: [M/F] ').upper().strip()[0]

while sex not in 'MmFf':
    sex = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()[0]

if sex == 'M':
    print(f'Sexo Masculino registrado com sucesso.')
elif sex == 'F':
    print(f'Sexo Feminino registrado com sucesso.')
    