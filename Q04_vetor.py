vetA = []
vetB = []
vetC = []
soma = 0

print('insira os valores do 1º vetor:')
print()
for c in range(0, 5):
    vetA.append(int(input(f'Digite um valor na posição {c}: ')))
print()
print('insira os valores do 2º vetor:')
print()   
for c in range(0, 5):
    vetB.append(int(input(f'Digite um valor na posição {c}: ')))
print()
for c in range(0, 5):
    soma = vetA[c] + vetB[c]
    vetC.append(soma)

print(f'O terceiro vetor com a soma dos dois primeiros vetores: {vetC}')