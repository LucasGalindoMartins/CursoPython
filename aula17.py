# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7) #Adiciona no final
# num.insert(2, 0) #Substitui
 
# print(num) 

# num.sort() #Ordena crescente
# print(num)

# num.sort(reverse=True) #Ordena descrescente
# print(num)

# num.pop(2) #Remove (pode escolhar a posição)
# print(num)

# num.remove(2) #Remove o primeiro valor que achar 
# print(num)

# if 4 in num:
#     num.remove(4)
# else:
#     print(f'Não achei o número 4 na lista')

# print(f'Essa lista tem {len(num)} elementos.')

# valores = []
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))

# for pos, v in enumerate(valores):
#     print(f'Na posição {pos} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a #Cria uma ligação
b = a[:] #Cria uma cópia
b[2] = 8

print(f'Lista a: {a}')
print(f'Lista b: {b}')