a = 3
b = 5
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretobranco': '\033[7;30m'}

print(f'Os valores são {cores['azul']}{a}{cores['limpa']} e {cores['amarelo']}{b}{cores['limpa']}')