statis = {}
gols = []
s = 0
statis['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {statis['nome']} jogou? '))

for p in range(0, partidas):
    gols.append(int(input(f'      Quantos gols na partida {p+1}? ')))
statis['gols'] = gols[:]
statis['total'] = sum(gols)
print('-='*30)

print(statis)
print('-='*30)

for k, v in statis.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {statis["nome"]} jogou {partidas} partidas.')
for pos, g in enumerate(gols):
    print(f'    => Na partida {pos+1}, fez {g} gols.')
print(f'Foi um total de {statis['total']} gols.')