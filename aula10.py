# nome = input('Qual o seu nome? ').strip()
# if nome == 'Lucas':
#     print('Que nome lindo!!')
# else:
#     print('Seu nome é normal!!')
# print(f'Bom dia, {nome}!')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')

print('PARABÉNS' if m>=6 else 'ESTUDE MAIS')

# if m >= 6:
#     print('Parabéns, vc foi aprovado!!')
# else:
#     print('Média insuficiente, vc foi reprovado!!')