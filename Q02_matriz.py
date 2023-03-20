matriz_A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz_A[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        soma += matriz_A[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        matriz_B[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        soma += matriz_B[l][c]
print('-=' * 30)
print(f'A soma das duas matrizes é: {soma}')
