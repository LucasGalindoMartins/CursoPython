name = input('Digite seu nome completo: ').strip()
n = name.split()

print('Muito prazer em te conhecer!!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n)- 1]}')