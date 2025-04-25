s = 0
i = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        s += c
        i += 1
print(f'A soma de todos os {i} valores solicitados é {s}')