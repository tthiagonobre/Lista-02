vet = []

print()
print('Digite 10 valores abaixo:')

for c in range(0, 10):
    vet.append(int(input(f'Digite um valor para a posição {c}: ')))
print()
print(f'Você digitou os valores: {vet}')
print()

print(f'Os elementos pares são: ')
for i in vet:
    if i % 2 == 0:
        print(i) 