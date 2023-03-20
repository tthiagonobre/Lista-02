vet = []
soma = 0

for c in range(0, 10):
    vet.append(int(input(f'Digite o valor na posição {c}: ')))

soma = sum(vet)    
    
print()
print(f'Os valores que você digitou foi: {vet}')
print()
print(f'A soma dos valores foi: {soma}')