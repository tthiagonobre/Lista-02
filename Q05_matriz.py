matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        valor = int(input(f"Digite o valor para a posição ({l},{c}): "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz original:")
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]: ^5}]', end=" ")
    print()

transposta = []
for l in range(3):
    linha = []
    for c in range(3):
        linha.append(matriz[c][l])
    transposta.append(linha)

print("Matriz transposta:")
for l in range(3):
    for c in range(3):
        print(f'[{matriz[c][l]: ^5}]', end=" ")
    print()
