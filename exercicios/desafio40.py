p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
m = (p1 + p2) / 2
print(f'''P1 = {p1}
P2 = {p2}  
MÉDIA = {m}  ''')

if m >= 6:
    print(f'Aluno \033[32mAPROVADO\033[m')
elif m <=5 and m < 6:
    print('O aluno está de \033[33mRECUPERAÇÃO\033[m')
else:
    print(f'O aluno foi \033[31mREPROVADO\033[m')