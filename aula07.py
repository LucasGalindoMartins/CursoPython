# Operações aritméticas
# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2.5
# 5 ** 2 = 25
# 25 ** (1/2) = 5
# 5 // 2 = 2
# 5 % 2 = 1

print('=' * 20)

name = input('Qual o seu nome: ')
print(f'Prazer em te conhecer {name:=^20}!')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m= n1 * n2
d = n1 / n2
di = n1 // n2
p= n1 ** n2

print(f'A soma é {s}, \n o produto é {m}, \n a divisão é {d:.3}, \n a divisão inteira é {di} \n e a pontecialização é {p}')
