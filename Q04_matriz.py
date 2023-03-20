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
    
simetrica = True
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] != matriz[c][l]:
            simetrica = False
            break
        
if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")
