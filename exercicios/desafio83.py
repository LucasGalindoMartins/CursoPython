# ex = input('Digite a expressão: ')
# n1 = ex.count('(')
# n2 = ex.count(')')
# s = n1 + n2
# if  s % 2 == 0:
#     print('Expressão válida!!')
# else:
#     print('Expressão inválida!!')

# COM O PROFESSOR

expr = input('Digite a expressão: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
    