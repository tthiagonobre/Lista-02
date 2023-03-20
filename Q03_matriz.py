matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
print('Sua matriz é: ')
print()

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]: ^5}]', end='')
    print()
print()

print('Diagonal principal: ')
for l in range(0, 4):
    print(f'[{matriz[l][l]: ^5}]', end='')
    