matriz = []

for l in range(0, 3):
    linha = []
    for c in range(0, 3):
        linha.append(int(input(f'Digite um valor para posição [{l}, {c}]: ')))
    matriz.append(linha)
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]: ^5}]', end='')
    print()
    