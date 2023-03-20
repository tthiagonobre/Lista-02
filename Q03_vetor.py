vet = []
maior = 0
menor = 0

for c in range(0, 10):
    vet.append(int(input(f'Digite o valor na posição {c}: ')))
    if c == 0:
        maior == menor == vet[c]
    else:
        if vet[c] > maior:
            maior = vet[c]
        if vet[c] < menor:
            menor = vet[c]
print()
print(f'Você digitou os valores: {vet}')
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')